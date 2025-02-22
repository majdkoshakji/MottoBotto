import logging

from discord import Message, Member

import MottoBotto

log = logging.getLogger("MottoBotto").getChild("reactions")
log.setLevel(logging.DEBUG)


async def skynet_prevention(botto: MottoBotto, message: Message):
    log.info(f"{message.author} attempted to activate Skynet!")
    await message.add_reaction(botto.config["reactions"]["reject"])
    await message.add_reaction(botto.config["reactions"]["skynet"])
    if botto.config["should_reply"]:
        await message.reply("Skynet prevention")


async def not_reply(botto: MottoBotto, message: Message):
    log.info(
        f"Suggestion from {message.author} was not a reply (Message ID {message.id})"
    )
    await message.add_reaction(botto.config["reactions"]["unknown"])
    if botto.config["should_reply"]:
        await message.reply("I see no motto!")


async def fishing(botto: MottoBotto, message: Message):
    log.info(f"Motto fishing from: {message.author}")
    await message.add_reaction(botto.config["reactions"]["reject"])
    await message.add_reaction(botto.config["reactions"]["fishing"])


async def invalid(botto: MottoBotto, message: Message):
    log.info(f"Motto from {message.author} is invalid according to rules.")
    await message.add_reaction(botto.config["reactions"]["reject"])
    await message.add_reaction(botto.config["reactions"]["invalid"])


async def duplicate(botto: MottoBotto, message: Message):
    log.debug("Ignoring motto, it's a duplicate.")
    await message.add_reaction(botto.config["reactions"]["repeat"])
    await message.remove_reaction(botto.config["reactions"]["pending"], botto.user)


async def deleted(botto: MottoBotto, message: Message):
    log.debug("Ignoring motto, it's been deleted.")
    await message.add_reaction(botto.config["reactions"]["deleted"])
    await message.add_reaction(botto.config["reactions"]["reject"])
    await message.remove_reaction(botto.config["reactions"]["pending"], botto.user)


async def stored(botto: MottoBotto, message: Message, motto_message: Message):
    await message.remove_reaction(botto.config["reactions"]["pending"], botto.user)
    await message.add_reaction(botto.config["reactions"]["success"])
    log.debug("Reaction added")
    if botto.config["should_reply"]:
        await message.reply(f'"{motto_message.content}" will be considered!')
    log.debug("Reply sent")


async def pending(botto: MottoBotto, message: Message, motto_message: Message):
    await message.add_reaction(botto.config["reactions"]["pending"])
    log.debug("Reaction added")


async def invalid_emoji(botto: MottoBotto, message: Message):
    log.info(f"Invalid emoji requested from {message.author}")
    await message.add_reaction(botto.config["reactions"]["invalid_emoji"])


async def valid_emoji(botto: MottoBotto, message: Message):
    log.info(f"Valid emoji requested from {message.author}")
    await message.add_reaction(botto.config["reactions"]["valid_emoji"])


async def unknown_dm(botto: MottoBotto, message: Message):
    log.info(f"I don't know how to handle {message.content} from {message.author}")
    await message.add_reaction(botto.config["reactions"]["unknown"])
