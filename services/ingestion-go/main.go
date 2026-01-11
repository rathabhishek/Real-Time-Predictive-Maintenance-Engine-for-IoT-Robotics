package main

import (
	"encoding/json"
	"math/rand"
	"time"
)

type SensorData struct {
	RobotID     string  `json:"robot_id"`
	Vibration   float64 `json:"vibration"`
	Temperature float64 `json:"temperature"`
	PowerLoad   float64 `json:"power_load"`
	Timestamp   int64   `json:"ts"`
}

func main() {
	// Logic to push simulated IoT data to Kinesis
	for {
		data := SensorData{
			RobotID:     "BOT-001",
			Vibration:   rand.Float64() * 10,
			Temperature: 60.0 + rand.Float64()*40.0,
			PowerLoad:   200.0 + rand.Float64()*50.0,
			Timestamp:   time.Now().Unix(),
		}
		payload, _ := json.Marshal(data)
		// push to Kinesis code here...
		time.Sleep(100 * time.Millisecond)
	}
}
