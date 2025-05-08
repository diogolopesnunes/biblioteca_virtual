from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "chave"

livros = []


@app.route("/")
def index():
    return render_template("index.html", livros=livros)


@app.route("/adicionar_livro", methods=["GET", "POST"])
def adicionar_livro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form["ano"]
        devolucao = request.form["devolucao"]
        livros.append([titulo, autor, ano, devolucao])
        flash("Livro adicionado com sucesso!")
        return redirect("/")
    return render_template("adicionar_livro.html")


@app.route("/editar_livro/<int:indice>", methods=["GET", "POST"])
def editar_livro(indice):
    livro = livros[indice]

    if request.method == "POST":
        livro[0] = request.form["titulo"]
        livro[1] = request.form["autor"]
        livro[2] = request.form["ano"]
        livro[3] = request.form["devolucao"]
        flash("Livro atualizado com sucesso!")
        return redirect("/")

    return render_template("editar_livro.html", livro=livro, indice=indice)


@app.route("/apagar_livro/<int:indice>")
def apagar_livro(indice):
    del livros[indice]
    flash("Livro removido com sucesso!")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)