pokemon_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "abilities": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "ability": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false,
                        "required": [
                            "name",
                            "url"
                        ]
                    },
                    "is_hidden": {
                        "type": "boolean"
                    },
                    "slot": {
                        "type": "integer"
                    }
                },
                "additionalProperties": false,
                "required": [
                    "ability",
                    "is_hidden",
                    "slot"
                ]
            }
        },
        "base_experience": {
            "type": "integer"
        },
        "cries": {
            "type": "object",
            "properties": {
                "latest": {
                    "type": "string"
                },
                "legacy": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "latest",
                "legacy"
            ]
        },
        "forms": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "url": {
                        "type": "string"
                    }
                },
                "additionalProperties": false,
                "required": [
                    "name",
                    "url"
                ]
            }
        },
        "game_indices": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "game_index": {
                        "type": "integer"
                    },
                    "version": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false,
                        "required": [
                            "name",
                            "url"
                        ]
                    }
                },
                "additionalProperties": false,
                "required": [
                    "game_index",
                    "version"
                ]
            }
        },
        "height": {
            "type": "integer"
        },
        "held_items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false,
                        "required": [
                            "name",
                            "url"
                        ]
                    },
                    "version_details": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "rarity": {
                                    "type": "integer"
                                },
                                "version": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "url": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "name",
                                        "url"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "rarity",
                                "version"
                            ]
                        }
                    }
                },
                "additionalProperties": false,
                "required": [
                    "item",
                    "version_details"
                ]
            }
        },
        "id": {
            "type": "integer"
        },
        "is_default": {
            "type": "boolean"
        },
        "location_area_encounters": {
            "type": "string"
        },
        "moves": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "move": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false,
                        "required": [
                            "name",
                            "url"
                        ]
                    },
                    "version_group_details": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "level_learned_at": {
                                    "type": "integer"
                                },
                                "move_learn_method": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "url": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "name",
                                        "url"
                                    ]
                                },
                                "order": {
                                    "type": "null"
                                },
                                "version_group": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "url": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "name",
                                        "url"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "level_learned_at",
                                "move_learn_method",
                                "version_group"
                            ]
                        }
                    }
                },
                "additionalProperties": false,
                "required": [
                    "move",
                    "version_group_details"
                ]
            }
        },
        "name": {
            "type": "string"
        },
        "order": {
            "type": "integer"
        },
        "past_abilities": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "abilities": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "ability": {
                                    "type": "null"
                                },
                                "is_hidden": {
                                    "type": "boolean"
                                },
                                "slot": {
                                    "type": "integer"
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "is_hidden",
                                "slot"
                            ]
                        }
                    },
                    "generation": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false,
                        "required": [
                            "name",
                            "url"
                        ]
                    }
                },
                "additionalProperties": false,
                "required": [
                    "abilities",
                    "generation"
                ]
            }
        },
        "past_types": {
            "type": "array"
        },
        "species": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "name",
                "url"
            ]
        },
        "sprites": {
            "type": "object",
            "properties": {
                "back_default": {
                    "type": "string"
                },
                "back_female": {
                    "type": "null"
                },
                "back_shiny": {
                    "type": "string"
                },
                "back_shiny_female": {
                    "type": "null"
                },
                "front_default": {
                    "type": "string"
                },
                "front_female": {
                    "type": "null"
                },
                "front_shiny": {
                    "type": "string"
                },
                "front_shiny_female": {
                    "type": "null"
                },
                "other": {
                    "type": "object",
                    "properties": {
                        "dream_world": {
                            "type": "object",
                            "properties": {
                                "front_default": {
                                    "type": "string"
                                },
                                "front_female": {
                                    "type": "null"
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "front_default"
                            ]
                        },
                        "home": {
                            "type": "object",
                            "properties": {
                                "front_default": {
                                    "type": "string"
                                },
                                "front_female": {
                                    "type": "null"
                                },
                                "front_shiny": {
                                    "type": "string"
                                },
                                "front_shiny_female": {
                                    "type": "null"
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "front_default",
                                "front_shiny"
                            ]
                        },
                        "official-artwork": {
                            "type": "object",
                            "properties": {
                                "front_default": {
                                    "type": "string"
                                },
                                "front_shiny": {
                                    "type": "string"
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "front_default",
                                "front_shiny"
                            ]
                        },
                        "showdown": {
                            "type": "object",
                            "properties": {
                                "back_default": {
                                    "type": "string"
                                },
                                "back_female": {
                                    "type": "null"
                                },
                                "back_shiny": {
                                    "type": "string"
                                },
                                "back_shiny_female": {
                                    "type": "null"
                                },
                                "front_default": {
                                    "type": "string"
                                },
                                "front_female": {
                                    "type": "null"
                                },
                                "front_shiny": {
                                    "type": "string"
                                },
                                "front_shiny_female": {
                                    "type": "null"
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "back_default",
                                "back_shiny",
                                "front_default",
                                "front_shiny"
                            ]
                        }
                    },
                    "additionalProperties": false,
                    "required": [
                        "dream_world",
                        "home",
                        "official-artwork",
                        "showdown"
                    ]
                },
                "versions": {
                    "type": "object",
                    "properties": {
                        "generation-i": {
                            "type": "object",
                            "properties": {
                                "red-blue": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_gray": {
                                            "type": "string"
                                        },
                                        "back_transparent": {
                                            "type": "string"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_gray": {
                                            "type": "string"
                                        },
                                        "front_transparent": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_gray",
                                        "back_transparent",
                                        "front_default",
                                        "front_gray",
                                        "front_transparent"
                                    ]
                                },
                                "yellow": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_gray": {
                                            "type": "string"
                                        },
                                        "back_transparent": {
                                            "type": "string"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_gray": {
                                            "type": "string"
                                        },
                                        "front_transparent": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_gray",
                                        "back_transparent",
                                        "front_default",
                                        "front_gray",
                                        "front_transparent"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "red-blue",
                                "yellow"
                            ]
                        },
                        "generation-ii": {
                            "type": "object",
                            "properties": {
                                "crystal": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "back_shiny_transparent": {
                                            "type": "string"
                                        },
                                        "back_transparent": {
                                            "type": "string"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_transparent": {
                                            "type": "string"
                                        },
                                        "front_transparent": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "back_shiny_transparent",
                                        "back_transparent",
                                        "front_default",
                                        "front_shiny",
                                        "front_shiny_transparent",
                                        "front_transparent"
                                    ]
                                },
                                "gold": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_transparent": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny",
                                        "front_transparent"
                                    ]
                                },
                                "silver": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_transparent": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny",
                                        "front_transparent"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "crystal",
                                "gold",
                                "silver"
                            ]
                        },
                        "generation-iii": {
                            "type": "object",
                            "properties": {
                                "emerald": {
                                    "type": "object",
                                    "properties": {
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "front_default",
                                        "front_shiny"
                                    ]
                                },
                                "firered-leafgreen": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny"
                                    ]
                                },
                                "ruby-sapphire": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "emerald",
                                "firered-leafgreen",
                                "ruby-sapphire"
                            ]
                        },
                        "generation-iv": {
                            "type": "object",
                            "properties": {
                                "diamond-pearl": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_female": {
                                            "type": "null"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "back_shiny_female": {
                                            "type": "null"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny"
                                    ]
                                },
                                "heartgold-soulsilver": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_female": {
                                            "type": "null"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "back_shiny_female": {
                                            "type": "null"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny"
                                    ]
                                },
                                "platinum": {
                                    "type": "object",
                                    "properties": {
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_female": {
                                            "type": "null"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "back_shiny_female": {
                                            "type": "null"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "diamond-pearl",
                                "heartgold-soulsilver",
                                "platinum"
                            ]
                        },
                        "generation-v": {
                            "type": "object",
                            "properties": {
                                "black-white": {
                                    "type": "object",
                                    "properties": {
                                        "animated": {
                                            "type": "object",
                                            "properties": {
                                                "back_default": {
                                                    "type": "string"
                                                },
                                                "back_female": {
                                                    "type": "null"
                                                },
                                                "back_shiny": {
                                                    "type": "string"
                                                },
                                                "back_shiny_female": {
                                                    "type": "null"
                                                },
                                                "front_default": {
                                                    "type": "string"
                                                },
                                                "front_female": {
                                                    "type": "null"
                                                },
                                                "front_shiny": {
                                                    "type": "string"
                                                },
                                                "front_shiny_female": {
                                                    "type": "null"
                                                }
                                            },
                                            "additionalProperties": false,
                                            "required": [
                                                "back_default",
                                                "back_shiny",
                                                "front_default",
                                                "front_shiny"
                                            ]
                                        },
                                        "back_default": {
                                            "type": "string"
                                        },
                                        "back_female": {
                                            "type": "null"
                                        },
                                        "back_shiny": {
                                            "type": "string"
                                        },
                                        "back_shiny_female": {
                                            "type": "null"
                                        },
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "animated",
                                        "back_default",
                                        "back_shiny",
                                        "front_default",
                                        "front_shiny"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "black-white"
                            ]
                        },
                        "generation-vi": {
                            "type": "object",
                            "properties": {
                                "omegaruby-alphasapphire": {
                                    "type": "object",
                                    "properties": {
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "front_default",
                                        "front_shiny"
                                    ]
                                },
                                "x-y": {
                                    "type": "object",
                                    "properties": {
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "front_default",
                                        "front_shiny"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "omegaruby-alphasapphire",
                                "x-y"
                            ]
                        },
                        "generation-vii": {
                            "type": "object",
                            "properties": {
                                "icons": {
                                    "type": "object",
                                    "properties": {
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "front_default"
                                    ]
                                },
                                "ultra-sun-ultra-moon": {
                                    "type": "object",
                                    "properties": {
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        },
                                        "front_shiny": {
                                            "type": "string"
                                        },
                                        "front_shiny_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "front_default",
                                        "front_shiny"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "icons",
                                "ultra-sun-ultra-moon"
                            ]
                        },
                        "generation-viii": {
                            "type": "object",
                            "properties": {
                                "icons": {
                                    "type": "object",
                                    "properties": {
                                        "front_default": {
                                            "type": "string"
                                        },
                                        "front_female": {
                                            "type": "null"
                                        }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                        "front_default"
                                    ]
                                }
                            },
                            "additionalProperties": false,
                            "required": [
                                "icons"
                            ]
                        }
                    },
                    "additionalProperties": false,
                    "required": [
                        "generation-i",
                        "generation-ii",
                        "generation-iii",
                        "generation-iv",
                        "generation-v",
                        "generation-vi",
                        "generation-vii",
                        "generation-viii"
                    ]
                }
            },
            "additionalProperties": false,
            "required": [
                "back_default",
                "back_shiny",
                "front_default",
                "front_shiny",
                "other",
                "versions"
            ]
        },
        "stats": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "base_stat": {
                        "type": "integer"
                    },
                    "effort": {
                        "type": "integer"
                    },
                    "stat": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false,
                        "required": [
                            "name",
                            "url"
                        ]
                    }
                },
                "additionalProperties": false,
                "required": [
                    "base_stat",
                    "effort",
                    "stat"
                ]
            }
        },
        "types": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "slot": {
                        "type": "integer"
                    },
                    "type": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false,
                        "required": [
                            "name",
                            "url"
                        ]
                    }
                },
                "additionalProperties": false,
                "required": [
                    "slot",
                    "type"
                ]
            }
        },
        "weight": {
            "type": "integer"
        }
    },
    "additionalProperties": false,
    "required": [
        "abilities",
        "base_experience",
        "cries",
        "forms",
        "game_indices",
        "height",
        "held_items",
        "id",
        "is_default",
        "location_area_encounters",
        "moves",
        "name",
        "order",
        "past_abilities",
        "past_types",
        "species",
        "sprites",
        "stats",
        "types",
        "weight"
    ]
}
