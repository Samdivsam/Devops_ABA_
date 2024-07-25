FROM python
WORKDIR /DEVOPS_ABA
COPY . /DEVOPS_ABA
EXPOSE 8000
CMD ["python", "serve_html.py"]
