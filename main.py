# Importing necessary libraries
import numpy as np

# Perceptron Learning Algorithm
def perceptron_learning(samples, labels, learning_rate=0.1, max_epochs=100):
    # Initialize weights (including bias as w0)
    weights = np.zeros(len(samples[0]))
    epochs = 0
    converged = False

    print("Initial weights:", weights)

    # Training loop
    while not converged and epochs < max_epochs:
        converged = True  # Assume convergence
        print(f"\nEpoch {epochs + 1}:")

        for i, sample in enumerate(samples):
            # Compute f(x) Evaluation Function
            fx = np.dot(weights, sample)
            # Compute g(x) Activation Function
            gx = 1 if fx > 0 else 0
            # Compute error
            error = labels[i] - gx

            print(f"Sample: {sample}, Target: {labels[i]}, f(x): {fx:.2f}, g(x): {gx}, Error: {error}")

            # Update weights if there is an error
            if error != 0:
                converged = False
                # Adjust weights
                #weights += learning_rate * error * np.array(sample)
                # Adjust weights without applying a learning rate
                weights += error * np.array(sample)
                print(f"Updated weights: {weights}")

        if converged:
            print("Error converged to 0 so the Weights converged.")
        epochs += 1

    return weights, epochs


# Input samples and labels
samples = np.array([
    [1, 0, 2],
    [1, 2, 0],
    [1, 1, 1],
    [1, 3, 0.5],
    [1, 1, 2.5]
])

labels = np.array([1, 0, 1, 0, 1])

# Run the perceptron learning algorithm
final_weights, total_epochs = perceptron_learning(samples, labels)

print("\nFinal weights:", final_weights)
print("Total epochs:", total_epochs)
