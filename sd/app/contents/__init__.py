"""SD application contents
"""
PROJECTNAME = "sd"

from Products.CMFCore.utils import ContentInit
from Products.Archetypes import process_types
from Products.Archetypes.public import listTypes


def at_processing(context):
    """Registers Archetypes content types
    """
    import document, paragraphs
    from security import DEFAULT_ADD_CONTENT_PERMISSION
    from security import ADD_CONTENT_PERMISSIONS

    contentTypes, constructors, ftis = process_types(listTypes(PROJECTNAME),
                                                     PROJECTNAME)

    ContentInit(
        PROJECTNAME + ' Content',
        content_types      = contentTypes,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    for i in range(0, len(contentTypes)):
        name = contentTypes[i].__name__
        if not name in ADD_CONTENT_PERMISSIONS:
            continue

        context.registerClass(meta_type    = ftis[i]['meta_type'],
                              constructors = (constructors[i],),
                              permission   = ADD_CONTENT_PERMISSIONS[name])

