from pixel_core import Panel, Layout

def set_puzzle_layout_10_5_5_snail():
        layout = Layout(10, 5, 5)

        layout.left_panel.set_h(0,[5,1])
        layout.left_panel.set_h(1,[2,2,2])
        layout.left_panel.set_h(2,[1,1,1])
        layout.left_panel.set_h(3,[1,3,4])
        layout.left_panel.set_h(4,[1,1,1,1,1])
        layout.left_panel.set_h(5,[1,1,1,1,2])
        layout.left_panel.set_h(6,[1,3,1])
        layout.left_panel.set_h(7,[6,1])
        layout.left_panel.set_h(8,[1,2])
        layout.left_panel.set_h(9,[7])

        layout.top_panel.set_v(0,[8])
        layout.top_panel.set_v(1,[2,1,1])
        layout.top_panel.set_v(2,[1,3,1,1])
        layout.top_panel.set_v(3,[1,1,1,1])
        layout.top_panel.set_v(4,[1,5,1])
        layout.top_panel.set_v(5,[2,2,1])
        layout.top_panel.set_v(6,[6,1])
        layout.top_panel.set_v(7,[1,2])
        layout.top_panel.set_v(8,[4,4])
        layout.top_panel.set_v(9,[1,3])

        layout.printLayout()
        return layout
