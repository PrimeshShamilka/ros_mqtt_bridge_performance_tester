# ros_mqtt_bridge_performance_tester
ROS MQTT bridge performance tester, using python

A tool for Network performance analysis and stress testing of ROS mqtt bridge and Rosbridge WebSocket. 

## How to run

## 1. Test for groove-x/mqtt bridge 

### launch mqtt bridge 

```
roslaunch mqtt_bridge demo.launch
```

### Initialize the listener node

```
python mqtt_msg_listener.py
```

### Initialize the talker node

```
python custom_ros_msg_talker.py
or
python pointcloud2_ros_talker.py
```

## 2. Test for rosbridge websocket 

### launch rosbridge websocket

```
roslaunch rosbridge_server rosbridge_websocket.launch
```

### Initialize the listener node using roslibjs_listener 

```
python -m http.server
```

### Initialize the talker node

```
python custom_ros_msg_talker.py
or
python pointcloud2_ros_talker.py
```

## Demo 

Pointcloud2 message and a custom message was used for the network analysis of groove-x/mqtt_bridge and Rosbridge WebSocket. For each message type network latency and packet loss were calculated at 10, 100, 1000, 10000, 100000 Hz frequencies. Each latency and packet loss value is an average of 5 values. 

Structure of the custom message is given below. 

Header header\
string name\
bool flag\
int8 age

### Analysis was carried out for 3 different setups. 

![](https://github.com/PrimeshShamilka/ros_mqtt_bridge_performance_tester/blob/master/images/setup1.png)

![](https://github.com/PrimeshShamilka/ros_mqtt_bridge_performance_tester/blob/master/images/setup2.png)

![](https://github.com/PrimeshShamilka/ros_mqtt_bridge_performance_tester/blob/master/images/setup3.png)

### Results from setup 1

![](https://github.com/PrimeshShamilka/ros_mqtt_bridge_performance_tester/blob/master/images/results1.png)

