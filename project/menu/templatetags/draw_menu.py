from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("draw_menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_path = request.path

    items = list(
        MenuItem.objects.filter(menu__name=menu_name)
        .select_related("parent", "menu")
    )

    active = None
    for item in items:
        if item.get_url() == current_path:
            active = item
            break

    items_ids = {item.id: item for item in items}
    root_items = []
    children = {}
    for item in items:
        if item.parent_id not in children:
            children[item.parent_id] = []
        children[item.parent_id].append(item)
        if item.parent is None:
            root_items.append(item)

    active_parents = set()
    if active:
        node = active
        while node and node.parent:
            active_parents.add(node.parent_id)
            node = items_ids.get(node.parent_id)

    tree = build_tree(root_items, active, active_parents, children)
    return {"menu_tree": tree, "name_menu": menu_name}


def build_tree(nodes, active, active_parents, children):
    tree = []
    for node in nodes:
        node_dict = {
            "item": node,
            "children": [],
            "has_child": False,
            "is_parent": (node.id in active_parents),
            "is_active": (node == active),
        }
        if node_dict["is_parent"]:
            node_dict["has_child"] = True
        if node_dict["is_active"]:
            node_dict["has_child"] = True

        node_children = children.get(node.id, [])
        node_dict["children"] = build_tree(node_children, active, active_parents, children)
        tree.append(node_dict)

    return tree
