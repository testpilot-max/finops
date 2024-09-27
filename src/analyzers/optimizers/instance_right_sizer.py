class InstanceRightSizer:
    def __init__(self, ec2_analyzer):
        self.ec2_analyzer = ec2_analyzer

    def suggest_instance_types(self):
        underutilized = self.ec2_analyzer.get_underutilized_instances()
        # Logic to suggest right-sized instances
        pass