import numpy as np
import matplotlib.pyplot as plt

def main():
    # Get user input for the mathematical expression
    expression = input("Enter a mathematical expression in terms of x (e.g., 'np.sin(x)', 'x**2'): ")

    # Generate x values
    x = np.linspace(-10, 10, 100)
    y = eval(expression)  # Evaluate the expression for y values

    # Create the plot
    plt.plot(x, y, label=f'y = {expression}', color='purple')
    plt.title('Magical Calculator Visualization')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()