// Logic to pre-process features before feeding into the ML model
public class SensorBatchAggregator implements AggregateFunction<SensorReading, FeatureBatch, FeatureBatch> {
    @Override
    public FeatureBatch add(SensorReading value, FeatureBatch accumulator) {
        // Collect vibration, temperature, and power into a time-series window
        accumulator.addReading(value.getVibration(), value.getTemperature(), value.getPowerLoad());
        return accumulator;
    }

    @Override
    public FeatureBatch getResult(FeatureBatch accumulator) {
        return accumulator; // Prepared window for LSTM
    }
}