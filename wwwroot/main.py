from flask import Flask, render_template, request, redirect, url_for
import db_handler
import mammoth
from config import Config


config = Config()


app = Flask(__name__, template_folder=f"{config.program_path}/templates", static_folder=f"{config.program_path}/static")

print (app.template_folder)


@app.route("/")
def hello_world():
    return redirect(url_for('handle_request'))


@app.route("/get_all_countries")
def get_countries():
    get_markdown("Словения")
    return db_handler.get_country_names()


@app.route("/country", methods=["GET"])
def handle_request():
    if request.method == 'GET':
        full_name = request.args.get('name')
        if full_name is None:
            return render_template('country-info-template.html')
        if full_name == '':
            return render_template('country-info-template.html')

        else:
            data = db_handler.get_data_by_country_name(full_name)
            data['guide'] = get_markdown(data['name'])
            if data is not None and data['name'] != '':
                return render_template('country-info-template.html', **data)
            else:
                return ''


def get_markdown(guide_id):
    try:
        guide_dir = f"{config.program_path}/static/guides/" + guide_id.lower().capitalize()
        guide_docx = db_handler.find_file_by_extension(guide_dir, 'docx')
        if guide_docx is None:
            return "гайд отсутствует"

        with open(f"{guide_dir}/{guide_docx}", "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_content = result.value
            return html_content
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=config.debug, port=config.port)