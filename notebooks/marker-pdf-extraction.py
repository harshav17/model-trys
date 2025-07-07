import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered
    return PdfConverter, create_model_dict, text_from_rendered


@app.cell
def _(PdfConverter, create_model_dict, text_from_rendered):
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )
    rendered = converter("./data/attention_paper.pdf")
    text, _, images = text_from_rendered(rendered)
    return images, text


@app.cell
def _(text):
    print(text)
    return


@app.cell
def _(images):
    print(images)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(images, mo):
    # Get the first image from the images dictionary
    first_key = list(images.keys())[0]
    first_img = images[first_key]
    mo.image(first_img)
    return


if __name__ == "__main__":
    app.run()
