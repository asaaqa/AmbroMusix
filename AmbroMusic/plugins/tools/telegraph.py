from telegraph import upload_file
from pyrogram import filters
from AmbroMusix import app


@app.on_message(filters.command('تلي'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("جاري الاستخراج...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' رابط تليكراف {url}')
