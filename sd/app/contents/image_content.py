# -*- coding: utf-8 -*-
from Products.ATContentTypes.content.image import ATImageSchema
from Products.Archetypes.public import (listTypes, DisplayList, Schema,
                                        StringField, SelectionWidget)

ORIGINAL_SIZE = (600,600)

TAG_SIZES = ATImageSchema['image'].sizes
TAG_VALUES = [(v, k, '%d x %d pixels' % v) for k, v in TAG_SIZES.items()]
TAG_VALUES.sort()
TAG_VALUES.reverse()
TAG_NAMES = DisplayList([ (k, label) for v, k, label in TAG_VALUES ])

tagselector = Schema((
    StringField('image_scale',
                required = False,
                default = "normal", 
                vocabulary = TAG_NAMES,
                widget = SelectionWidget(label="Size of the image",
                                         label_msgid="label_sizes",
                                         default="thumb",
                                         description=("Size of the thumbnail "
                                                      "displayed in the "
                                                      "paragraph's body"),
                                         description_msgid="desc_sizes",
                                         i18n_domain='sd',
                                         )),
    ))

