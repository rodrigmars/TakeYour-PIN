from markdown import markdown
from pygments.formatters import HtmlFormatter
# from typing import Callable


def home_controller(markdown_api: str) -> dict:

    def home() -> tuple | None:

        try:

            with open(markdown_api, 'r') as mkd:
                template_html = markdown(mkd.read(), extensions=["fenced_code"])

        except Exception as ex:
            print("ERRO", ex)

        else:

            print("md_template", template_html)

            formatter = HtmlFormatter(
                style="zenburn", full=True, cssclass="codehilite")
            css_string = formatter.get_style_defs()
            md_css_string = "<style>" + css_string + "</style>"

            html = md_css_string + template_html

            print(html)

            return html

    return {"home": home}
