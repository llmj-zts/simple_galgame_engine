import pygame
import glob
import os.path
from typing import Dict
from game.config import Path, Display


def load_all_figure() -> Dict[str, pygame.Surface]:
    image_dict = {}
    for image_name in glob.glob(os.path.join(Path.PATH_IMAGE, "figure", "*.png")):
        image_dict[os.path.basename(image_name).split(".")[0]] = pygame.image.load(
            image_name
        ).convert_alpha()
    return image_dict


def load_background(text: str) -> pygame.Surface:
    if text[-3:] not in ["png", "jpg"]:
        text += ".png"
    image = pygame.image.load(
        os.path.join(Path.PATH_IMAGE_BACKGROUND, text)
    ).convert_alpha()
    image = pygame.transform.scale(image, (Display.WIDTH, Display.HEIGHT))
    return image


def load_ui(text: str) -> pygame.Surface:
    image = pygame.image.load(os.path.join(Path.PATH_IMAGE_UI, text)).convert_alpha()
    return image


def load_transition(text: str) -> pygame.Surface:
    if text[-3:] not in ["png", "jpg"]:
        text += ".png"
    image = pygame.image.load(
        os.path.join(Path.PATH_IMAGE_TRANSITION, text)
    ).convert_alpha()
    image = pygame.transform.scale(image, (Display.WIDTH, Display.HEIGHT))
    return image
