from fastapi import FastAPI

from gradio_animate import demo

app = FastAPI()
app = gr.mount_gradio_app(app, demo, "/")


if __name__ == "__main__":
    import logging
    from argparse import ArgumentParser

    import uvicorn

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    parser = ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    uvicorn.run(app, host="127.0.0.1", port=args.port)
