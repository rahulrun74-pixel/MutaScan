def color_alignment(ref, sample):

    colored_ref = []
    colored_sample = []
    marker = []

    for r, s in zip(ref, sample):

        if r == s:
            colored_ref.append(f"[{r}]")
            colored_sample.append(f"[{s}]")
            marker.append("|")

        elif r == "-" or s == "-":
            colored_ref.append(f"({r})")
            colored_sample.append(f"({s})")
            marker.append(" ")

        else:
            colored_ref.append(f"{{{r}}}")
            colored_sample.append(f"{{{s}}}")
            marker.append("*")

    return (
        " ".join(colored_ref),
        " ".join(marker),
        " ".join(colored_sample)
    )