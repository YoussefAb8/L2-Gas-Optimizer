# L2-Gas-Optimizer
An AI-driven regression model developed to analyze network activity and predict optimal gas prices for decentralized transactions, particularly for Layer 2 scaling solutions. By leveraging a RandomForestRegressor, this tool processes key on-chain indicators to generate an estimated optimal gas price, providing valuable insights to help DeFi users minimize transaction costs and improve transaction speed.

Project Status: Testnet

This model is currently deployed and tested on the OpenGradient Testnet.

# How it Works

The model evaluates network conditions based on 2 core features to determine its status:

Network Congestion: A metric representing the current level of activity or transaction queue on the network.

Base Fee Trend: A representation of the recent trend (e.g., historical average) of the base fee.

The model generates a single predicted value:

Estimated Optimal Gas Price (e.g., in Gwei).

On-chain Validation (Proof of Execution)

Here is a screenshot showing the successful inference of the Apex Gas Price Optimizer model on the OpenGradient Testnet.
<img width="1353" height="601" alt="image" src="https://github.com/user-attachments/assets/3959577e-2333-4af7-80d7-9979f077d0c4" />
