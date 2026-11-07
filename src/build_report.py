"""Render reports/final_report.md -> reports/final_report.html -> reports/final_report.pdf (via headless Chrome)."""
import pathlib, subprocess, markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 18mm 17mm 18mm 17mm; }
body { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #000; }
h1 { font-size: 30pt; color: #000; margin: 0 0 10px; line-height: 1.15; }
h2 { font-size: 17pt; color: #000; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-top: 4px; }
h3 { font-size: 12.5pt; color: #000; margin: 16px 0 6px; page-break-after: avoid; }
p, li { text-align: left; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9.3pt; page-break-inside: avoid; }
th { color: #000; text-align: left; padding: 5px 7px; border-top: 1.5px solid #000; border-bottom: 1px solid #000; }
td { border-bottom: 0.5px solid #999; padding: 4px 7px; vertical-align: top; }
img { display: block; max-width: 92%; max-height: 300px; margin: 8px auto 6px; page-break-inside: avoid; }
blockquote { border-left: 2px solid #000; margin: 10px 0; padding: 4px 14px; font-style: italic; }
code { font-family: Menlo, monospace; font-size: 9pt; }
.page-break { page-break-after: always; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; }
.cover .course { color: #000; font-weight: bold; letter-spacing: .05em; text-transform: uppercase; font-size: 10pt; }
.cover .subtitle { font-size: 15pt; color: #000; max-width: 150mm; }
.cover .team { margin-top: 40mm; font-size: 11pt; color: #000; }
"""

def main():
    md = (REPORTS / "final_report.md").read_text()
    body = markdown.markdown(md, extensions=["tables", "md_in_html"])
    html = f"<!doctype html><html><head><meta charset='utf-8'><title>Predicting Hotel Booking Cancellations</title><style>{CSS}</style></head><body>{body}</body></html>"
    out_html = REPORTS / "final_report.html"
    out_html.write_text(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={REPORTS / 'final_report.pdf'}", out_html.as_uri()], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Wrote", REPORTS / "final_report.pdf")

if __name__ == "__main__":
    main()
