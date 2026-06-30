from Bio import SeqIO
from io import StringIO

def read_fasta(file):
    """
    Reads a FASTA file from Streamlit uploader or local file.
    Returns the first sequence.
    """

    try:

        # Streamlit UploadedFile
        if hasattr(file, "read"):

            content = file.read()

            if isinstance(content, bytes):
                content = content.decode("utf-8")

            handle = StringIO(content)

            record = next(SeqIO.parse(handle, "fasta"))

            return str(record.seq).upper()

        # Local filename
        else:

            record = next(SeqIO.parse(file, "fasta"))

            return str(record.seq).upper()

    except Exception as e:
        print(e)
        return None