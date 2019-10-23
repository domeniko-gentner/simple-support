<html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css.css') }}">
    </head>
<body>
    <h1 style="margin-top: 2vh;">Anfrage an die IT</h1>
    <form action="send-email" method="POST">
        <label for="form-subject">Betreff
        <input type="text" name="form-subject" placeholder="Bitte den Betreff eingeben">
        </label>

        <label for="form-employee">Name
        <input type="text" name="form-employee" placeholder="Bitte deinen Namen eingeben...">
        </label>

        <label for="form-room">Zimmer Nr
        <input type="text" name="form-room" placeholder="Bitte Zimmer Nr. eingeben...">
        </label>

        <label for="form-body">Nachricht</label>
        <textarea rows=25 name="form-body" placeholder="Bitte Nachricht eingeben...">
        </textarea>

        <input type="submit" value="Senden">
    </form>
</body>
</html>
