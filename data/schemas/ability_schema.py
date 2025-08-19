ability_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "effect_changes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "effect_entries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "effect": {
                                    "type": "string"
                                },
                                "language": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "url": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": False,
                                    "required": [
                                        "name",
                                        "url"
                                    ]
                                }
                            },
                            "additionalProperties": False,
                            "required": [
                                "effect",
                                "language"
                            ]
                        }
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
                        "additionalProperties": False,
                        "required": [
                            "name",
                            "url"
                        ]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "effect_entries",
                    "version_group"
                ]
            }
        },
        "effect_entries": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "effect": {
                        "type": "string"
                    },
                    "language": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "name",
                            "url"
                        ]
                    },
                    "short_effect": {
                        "type": "string"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "effect",
                    "language",
                    "short_effect"
                ]
            }
        },
        "flavor_text_entries": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "flavor_text": {
                        "type": "string"
                    },
                    "language": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "name",
                            "url"
                        ]
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
                        "additionalProperties": False,
                        "required": [
                            "name",
                            "url"
                        ]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "flavor_text",
                    "language",
                    "version_group"
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
            "additionalProperties": False,
            "required": [
                "name",
                "url"
            ]
        },
        "id": {
            "type": "integer"
        },
        "is_main_series": {
            "type": "boolean"
        },
        "name": {
            "type": "string"
        },
        "names": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "language": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "name",
                            "url"
                        ]
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "language",
                    "name"
                ]
            }
        },
        "pokemon": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "is_hidden": {
                        "type": "boolean"
                    },
                    "pokemon": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "url": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "name",
                            "url"
                        ]
                    },
                    "slot": {
                        "type": "integer"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "is_hidden",
                    "pokemon",
                    "slot"
                ]
            }
        }
    },
    "additionalProperties": False,
    "required": [
        "effect_changes",
        "effect_entries",
        "flavor_text_entries",
        "generation",
        "id",
        "is_main_series",
        "name",
        "names",
        "pokemon"
    ]
}