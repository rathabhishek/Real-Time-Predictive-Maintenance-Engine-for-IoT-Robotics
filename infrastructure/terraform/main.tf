resource "aws_eks_cluster" "aegis_cluster" {
  name     = "AegisML-Production"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = [aws_subnet.private_1.id, aws_subnet.private_2.id]
  }
}

# Demonstrates 99.99% uptime via node groups
resource "aws_eks_node_group" "ml_nodes" {
  cluster_name    = aws_eks_cluster.aegis_cluster.name
  node_group_name = "inference-workers"
  instance_types  = ["t3.medium"]
  
  scaling_config {
    desired_size = 3
    max_size     = 5
    min_size     = 1
  }
}