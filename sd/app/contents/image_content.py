# -*- coding: utf-8 -*-
from Products.ATContentTypes.content.image import ATImageSchema
from Products.Archetypes.public import (listTypes, DisplayList, Schema,
                                        StringField, SelectionWidget)

ORIGINAL_SIZE = (600,600)

TAG_SIZES = ATImageSchema['image'].sizes
TAG_NAMES = DisplayList((lambda l: (l.sort(), l.reverse(), l)[2])
                        ([(k, '%d x %d pixels' % v) for k, v
                          in TAG_SIZES.items()]))

tagselector = Schema((
    StringField('image_scale',
                required = False,
                default = "normal", 
                vocabulary = TAG_NAMES,
                widget = SelectionWidget(label="Size of the image",
                                         label_msgid="label_sizes",
                                         description=("Size of the thumbnail "
                                                      "displayed in the "
                                                      "paragraph's body"),
                                         description_msgid="desc_sizes",
                                         i18n_domain='sd',
                                         )),
    ))

