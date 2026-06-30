import streamlit as st
import pandas as pd
import plotly.express as px

from modules.fasta_reader import read_fasta
from modules.mutation_detector import detect_mutations
from modules.gc_content import calculate_gc
from modules.translator import translate_dna
from modules.reverse_complement import reverse_complement
from modules.charts import mutation_chart
from modules.alignment_viewer import build_alignment
from modules.report import generate_report   # ✅ ADDED

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="MutaScan - DNA Mutation Analyzer",
    page_icon="🧬",
    layout="wide"
)

# =========================
# CUSTOM HEADER (NEW UI)
# =========================

st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #00D4FF;
        text-align: center;
    }
    .sub-title {
        font-size: 18px;
        color: #A0A0A0;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧬 MutaScan</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Advanced DNA Mutation Analysis Platform</div>', unsafe_allow_html=True)

st.markdown("---")

# =========================
# SIDEBAR
# =========================

st.sidebar.header("📂 Upload FASTA Files")

reference_file = st.sidebar.file_uploader(
    "Upload Reference FASTA",
    type=["fasta", "fa", "fna"]
)

sample_file = st.sidebar.file_uploader(
    "Upload Sample FASTA",
    type=["fasta", "fa", "fna"]
)

st.sidebar.info("Upload two FASTA files to begin analysis.")

# =========================
# MAIN LOGIC
# =========================

if reference_file and sample_file:

    reference = read_fasta(reference_file)
    sample = read_fasta(sample_file)

    if not reference or not sample:
        st.error("Error reading FASTA files.")
        st.stop()

    aligned_ref, aligned_sample, mutations, summary = detect_mutations(
        reference,
        sample
    )

    # =========================
    # ALIGNMENT DISPLAY
    # =========================

    st.header("🧬 Sequence Alignment")

    marker = build_alignment(aligned_ref, aligned_sample)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Reference")
        st.code(aligned_ref)

    with col2:
        st.subheader("Match Map")
        st.code(marker)

    with col3:
        st.subheader("Sample")
        st.code(aligned_sample)

    st.markdown("---")

    # =========================
    # METRICS
    # =========================

    st.header("📊 Mutation Summary")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Substitutions", summary["Substitution"])
    c2.metric("Insertions", summary["Insertion"])
    c3.metric("Deletions", summary["Deletion"])
    c4.metric("Total", summary["Total"])
    c5.metric("Alignment Score", summary["Alignment Score"])

    st.markdown("---")

    # =========================
    # CHARTS
    # =========================

    st.header("📈 Mutation Distribution")

    fig = mutation_chart(summary)
    st.plotly_chart(fig, use_container_width=True)

    gc_df = pd.DataFrame({
        "Sequence": ["Reference", "Sample"],
        "GC Content": [
            calculate_gc(reference),
            calculate_gc(sample)
        ]
    })

    fig2 = px.bar(
        gc_df,
        x="Sequence",
        y="GC Content",
        title="GC Content Comparison",
        text="GC Content"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # =========================
    # SEQUENCE ANALYSIS
    # =========================

    st.header("🧪 Sequence Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Reference")
        st.write("Length:", len(reference))
        st.write("GC Content:", calculate_gc(reference), "%")
        st.text_area("Protein", translate_dna(reference), height=150)

    with col2:
        st.subheader("Sample")
        st.write("Length:", len(sample))
        st.write("GC Content:", calculate_gc(sample), "%")
        st.text_area("Protein", translate_dna(sample), height=150)

    st.markdown("---")

    # =========================
    # REVERSE COMPLEMENT
    # =========================

    st.header("🔄 Reverse Complement")

    st.text_area(
        "Reference Reverse Complement",
        reverse_complement(reference),
        height=120
    )

    st.markdown("---")

    # =========================
    # MUTATION TABLE
    # =========================

    st.header("📋 Mutation Table")

    if len(mutations) == 0:
        st.success("No mutations detected 🎉")
    else:
        df = pd.DataFrame(mutations)

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False)

        st.download_button(
            "📥 Download CSV",
            csv,
            file_name="mutascan_report.csv",
            mime="text/csv"
        )

    st.markdown("---")

    # =========================
    # PDF REPORT SECTION (NEW)
    # =========================

    st.header("📄 Report Generation")

    if st.button("Generate PDF Report"):

        file_path = generate_report(summary)

        with open(file_path, "rb") as f:
            st.download_button(
                "⬇ Download PDF Report",
                f,
                file_name="MutaScan_Report.pdf",
                mime="application/pdf"
            )

    # =========================
    # FOOTER
    # =========================

    st.markdown("""
    ---
    🧬 MutaScan v3.0 | Built with Streamlit + BioPython + Needleman-Wunsch
    """)

else:
    st.info("⬅ Upload both FASTA files to start analysis.")