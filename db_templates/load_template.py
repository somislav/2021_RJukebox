from jinja2 import Environment, FileSystemLoader
import logging


def load_db_template(template_name: str):
    logging.info(f"Loading template: {template_name}")
    try:
        environment = Environment(loader=FileSystemLoader(os.getenv("DB_TEMPLATES")))
        template = environment.get_template(template_name)
        return template
    except Exception as e:
        logging.error(f"Exception happened while paprsing template [{template_name}]: {e}")
        return None
