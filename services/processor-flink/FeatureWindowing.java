// Real-time windowing for LSTM features
public class FeatureWindowing {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        
        // Consuming from Kinesis telemetry
        DataStream<SensorReading> rawStream = env.addSource(new FlinkKinesisConsumer<>(...));

        // Create 50-step sliding windows for deep learning inference
        DataStream<FeatureBatch> windowedStream = rawStream
            .keyBy(SensorReading::getRobotId)
            .countWindow(50, 1) 
            .aggregate(new BatchAggregator());

        windowedStream.addSink(new KinesisSink<>(...));
        env.execute("AegisML-Feature-Aggregator");
    }
}