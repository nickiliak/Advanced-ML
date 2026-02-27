"""
Plotting and evaluation utilities for Week1 VAE exercise.
"""

import torch
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import os


def evaluate_elbo(model, test_loader, device):
    """
    Evaluate the ELBO on the test set.
    
    Parameters:
    model: VAE model
    test_loader: DataLoader for test set
    device: torch device
    
    Returns:
    mean_elbo: Average ELBO across all test samples
    """
    model.eval()
    total_elbo = 0.0
    num_samples = 0
    
    with torch.no_grad():
        for x, _ in test_loader:
            x = x[0].to(device) if isinstance(x, (list, tuple)) else x.to(device)
            elbo = model.elbo(x)
            total_elbo += elbo.item() * x.size(0)
            num_samples += x.size(0)
    
    mean_elbo = total_elbo / num_samples
    print(f"Test Set ELBO: {mean_elbo:.4f}")
    return mean_elbo


def plot_aggregate_posterior(model, test_loader, latent_dim, device, save_path=None):
    """
    Plot samples from the approximate posterior colored by class label.
    
    Parameters:
    model: VAE model
    test_loader: DataLoader for test set
    latent_dim: Dimension of latent space (M)
    device: torch device
    save_path: Optional path to save the figure
    """
    model.eval()
    all_samples = []
    all_labels = []
    
    with torch.no_grad():
        for x, y in test_loader:
            x = x[0].to(device) if isinstance(x, (list, tuple)) else x.to(device)
            q = model.encoder(x)
            z = q.rsample()  # Sample from approximate posterior
            all_samples.append(z.cpu().numpy())
            all_labels.append(y.numpy())
    
    # Concatenate all samples and labels
    samples = np.concatenate(all_samples, axis=0)
    labels = np.concatenate(all_labels, axis=0)
    
    # Apply PCA if latent_dim > 2
    if latent_dim > 2:
        pca = PCA(n_components=2)
        samples = pca.fit_transform(samples)
        xlabel = f'PC1 ({pca.explained_variance_ratio_[0]:.1%})'
        ylabel = f'PC2 ({pca.explained_variance_ratio_[1]:.1%})'
    else:
        xlabel = 'Latent Dimension 0'
        ylabel = 'Latent Dimension 1'
    
    # Plot
    plt.figure(figsize=(12, 9))
    scatter = plt.scatter(samples[:, 0], samples[:, 1], c=labels, cmap='tab10', alpha=0.6, s=30)
    plt.colorbar(scatter, label='Class Label', ticks=range(10))
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title('Aggregate Posterior Samples from Test Set', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        os.makedirs(os.path.dirname(save_path) or 'Week1/outputs', exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Figure saved to {save_path}")
    
    plt.show()


def plot_aggregate_posterior_subplots(model, test_loader, latent_dim, device, save_path=None):
    """
    Plot samples from the approximate posterior in a grid with one subplot per class.
    
    Parameters:
    model: VAE model
    test_loader: DataLoader for test set
    latent_dim: Dimension of latent space (M)
    device: torch device
    save_path: Optional path to save the figure
    """
    model.eval()
    all_samples = []
    all_labels = []
    
    with torch.no_grad():
        for x, y in test_loader:
            x = x[0].to(device) if isinstance(x, (list, tuple)) else x.to(device)
            q = model.encoder(x)
            z = q.rsample()  # Sample from approximate posterior
            all_samples.append(z.cpu().numpy())
            all_labels.append(y.numpy())
    
    # Concatenate all samples and labels
    samples = np.concatenate(all_samples, axis=0)
    labels = np.concatenate(all_labels, axis=0)
    
    # Apply PCA if latent_dim > 2
    if latent_dim > 2:
        pca = PCA(n_components=2)
        samples = pca.fit_transform(samples)
        xlabel = f'PC1 ({pca.explained_variance_ratio_[0]:.1%})'
        ylabel = f'PC2 ({pca.explained_variance_ratio_[1]:.1%})'
    else:
        xlabel = 'Latent Dimension 0'
        ylabel = 'Latent Dimension 1'
    
    # Plot with subplots for each class
    fig, axes = plt.subplots(2, 5, figsize=(16, 8))
    axes = axes.flatten()
    colors = plt.cm.tab10(np.linspace(0, 1, 10))
    
    for digit in range(10):
        ax = axes[digit]
        mask = labels == digit
        ax.scatter(samples[mask, 0], samples[mask, 1], c=[colors[digit]], alpha=0.6, s=30)
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_title(f'Class {digit}', fontsize=12)
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path) or 'Week1/outputs', exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Figure saved to {save_path}")
    
    plt.show()
