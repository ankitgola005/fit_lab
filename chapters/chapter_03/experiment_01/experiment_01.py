import numpy as np
import matplotlib.pyplot as plt
import os

from fit_lab.utils import generate_data, polynomial_basis, solve_ls

# ------------------------
# Metrics
# ------------------------
def mse(y, t):
    return np.mean((y - t)**2)


# ------------------------
# Main
# ------------------------
def run_experiment():
    os.makedirs("plots", exist_ok=True)

    degrees = [x for x in range(0, 4)]
    degrees += [x for x in range(4, 17, 4)]

    x, t, y_true = generate_data()
    x_plot = np.linspace(-1, 1, 200).reshape(-1, 1)
    y_true_plot = np.sin(2 * np.pi * x_plot)

    train_errors = []
    cond_numbers = []
    all_preds = {}

    print("\n=== Results ===")

    for d in degrees:
        Phi = polynomial_basis(x, d)
        w = solve_ls(Phi, t)

        Phi_plot = polynomial_basis(x_plot, d)
        y_pred = Phi_plot @ w
        train_pred = Phi @ w

        train_mse = mse(train_pred, t)
        cond = np.linalg.cond(Phi.T @ Phi)

        train_errors.append(train_mse)
        cond_numbers.append(cond)
        all_preds[d] = y_pred

        print(f"\nDegree {d}")
        print(f"Train MSE: {train_mse:.6f}")
        print(f"Condition Number: {cond:.2e}")

        # Individual plots
        plt.figure()
        plt.scatter(x, t, label="Data")
        plt.plot(x_plot, y_true_plot, label="True Function")
        plt.plot(x_plot, y_pred, label=f"Model (deg={d})")
        plt.legend()
        plt.title(f"Polynomial Degree {d}")
        plt.savefig(f"plots/degree_{d}.png")
        plt.close()

    # ------------------------
    # Combined Plot
    # ------------------------
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(x, t, label="Data")
    ax.plot(x_plot, y_true_plot, label="True Function", linewidth=2)

    for d in degrees:
        ax.plot(x_plot, all_preds[d], label=f"deg={d}")

    ax.set_title("Model Comparison Across Degrees")

    # Shrink plot area to leave space on the right
    ax.set_position([0.1, 0.1, 0.6, 0.8])  # [left, bottom, width, height]
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), borderaxespad=0)
    plt.savefig("plots/combined.png", bbox_inches="tight")
    plt.close()

    # ------------------------
    # Train Error Plot
    # ------------------------
    plt.figure()
    plt.plot(degrees, train_errors, marker='o')
    plt.xlabel("Degree")
    plt.ylabel("Train MSE")
    plt.title("Training Error vs Model Complexity")
    plt.savefig("plots/train_error.png")
    plt.close()


if __name__ == "__main__":
    run_experiment()