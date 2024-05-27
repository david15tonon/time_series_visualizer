from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Import the tests
import test_module

# Run the tests
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    test_module.run_tests()
