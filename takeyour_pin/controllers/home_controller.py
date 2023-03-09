from markdown import markdown
from pygments.formatters import HtmlFormatter
# from typing import Callable


def home_controller(markdown_api: str) -> dict:

    def home() -> str:

        html_: str = ""

        try:

            with open(markdown_api, 'r') as mkd:
                template_html = markdown(mkd.read(), extensions=[
                                         "fenced_code", "codehilite"])

        except Exception as ex:
            print("ERRO", ex)

        else:

            formatter = HtmlFormatter(
                style="zenburn", full=True, cssclass="codehilite")

            md_css_string = f"<style>{formatter.get_style_defs()}</style>"

            html_ = md_css_string + template_html

        return html_

    return {"home": home}
