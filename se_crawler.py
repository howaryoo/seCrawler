import connexion

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('seCrawler.yaml')

if __name__ == '__main__':
    app.run(port=8080)
