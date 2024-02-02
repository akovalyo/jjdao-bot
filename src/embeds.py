import discord


class EmbedFactory:
    def __init__(
        self,
        color,
        description: str,
        title="Solsuite",
        url="",
        image="",
        footer_text="Powered by JellyCo",
        footer_icon="https://i.imgur.com/qMYLbZG.jpeg",
        thumbnail="",
        author_name="",
        author_icon="",
        author_url="",
        fields=[],
    ):
        self.color = 0x1E1F1E
        if title == "empty":
            self.title = "\u200b"
        else:
            self.title = title
        self.url = url
        self.image = image
        self.description = "\u200b" if description == "empty" else description
        if footer_text == "empty":
            self.footer_text = "\u200b"
        else:
            self.footer_text = footer_text
        self.footer_icon = footer_icon
        self.thumbnail = thumbnail
        self.author_name = author_name
        self.author_icon = author_icon
        self.author_url = author_url
        self.fields = fields

        self.set_color(color)

    def set_color(self, color):
        if type(color) == str:
            match color:
                case "error":
                    color = 0xFF0000
                case "ok":
                    color = 0x008000
                case "pending":
                    color = 0xDDE32B
                case "ended":
                    color = 0x352836
                case "jelly":
                    color = 0x9F1DDB
                case _:
                    color = 0x1E1F1E
        self.color = color

    def create(self):
        embed = discord.Embed(
            title=self.title,
            color=self.color,
            description=self.description,
            url=self.url,
        )
        embed.set_footer(text=self.footer_text, icon_url=self.footer_icon)
        if self.thumbnail:
            embed.set_thumbnail(url=self.thumbnail)
        if self.author_name:
            embed.set_author(
                name=self.author_name, icon_url=self.author_icon, url=self.author_url
            )
        if self.image:
            embed.set_image(url=self.image)
        for field in self.fields:
            inline = False
            if len(field) == 3:
                inline = field[2]
            name = "\u200b" if field[0] == "empty" else field[0]
            value = "\u200b" if field[1] == "empty" else field[1]
            embed.add_field(name=name, value=value, inline=inline)
        return embed

    def empty_field_converter(self, field: tuple) -> tuple:
        if field[0] == "empty":
            field = tuple("\u200b", field[1])
        if field[1] == "empty":
            field = tuple(field[0], "\u200b")
        return field

    def add_field(self, field: tuple):
        self.fields.append(field)

    def set_fields(self, fields: list):
        self.fields = fields
