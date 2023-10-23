import boto3

cloudwatch = boto3.client('cloudwatch')

# Define los parámetros para la alerta
alarm_name = 'MiAlarma'
metric_name = 'CPUUtilization'
namespace = 'AWS/EC2'
comparison_operator = 'GreaterThanThreshold'
threshold = 80.0
period = 300
evaluation_periods = 1
alarm_description = 'Alarma cuando la CPU supera el 80%'

# Crea la alarma
response = cloudwatch.put_metric_alarm(
    AlarmName=alarm_name,
    ComparisonOperator=comparison_operator,
    EvaluationPeriods=evaluation_periods,
    MetricName=metric_name,
    Namespace=namespace,
    Period=period,
    Statistic='Average',
    Threshold=threshold,
    AlarmDescription=alarm_description,
 
)

print("Alerta creada:", response)