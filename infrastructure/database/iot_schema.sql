-- Schema for real-time tracking (Reflects Vanguard asset management operations) [cite: 13]
CREATE TABLE robot_health_logs (
    log_id UUID PRIMARY KEY,
    robot_id VARCHAR(50) NOT NULL,
    vibration_index FLOAT,
    failure_probability DECIMAL(5, 4),
    predicted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_robot_id ON robot_health_logs(robot_id);