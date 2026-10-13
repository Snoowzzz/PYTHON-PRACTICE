# IoT Lab Viva Quick-Revision Guide
**Topics:** Ubidots monitoring • IoT cloud/ThingSpeak • Raspberry Pi web server • Arduino–Bluetooth Android control  
**Style:** Short viva answers, definitions, key terms, workflows, and likely follow-up questions.

> **How to use this today:** Read the “30-second overview” for each lab first. Then revise the keywords and say the Q&A answers aloud. If asked to explain a diagram, describe the signal flow from left to right.

---

## 0. Core IoT terms you can be asked in any lab

| Keyword | Short meaning |
|---|---|
| **IoT (Internet of Things)** | Physical devices with sensors/actuators, processing, and network connectivity that collect or exchange data. |
| **Sensor** | Converts a physical quantity such as temperature into a readable signal/data value. |
| **Actuator** | Performs an action, e.g., switches an LED, bulb, motor, or relay. |
| **Microcontroller** | Small computer on a chip that runs a control program; Arduino Uno is a common example. |
| **SBC (Single-Board Computer)** | Complete small computer on one board; Raspberry Pi is an example. |
| **Edge device** | Device near the source of data that can collect, process, or act on data locally. |
| **Gateway** | Connects devices/networks or protocols and can forward data to another system or cloud. |
| **Cloud** | Remote computing and storage accessed over a network. |
| **Telemetry** | Measurements/status sent from a device to another system. |
| **Dashboard** | Visual display of device values, charts, gauges, and status. |
| **API** | Defined interface that lets software systems exchange data or request actions. |
| **Protocol** | Rules/format used for communication, such as HTTP, MQTT, or Bluetooth. |
| **Latency** | Time taken for data or a command to travel and be acted upon. |
| **Real-time monitoring** | Observing current or frequently updated device data. |
| **Authentication** | Checking who or what is connecting. |
| **Authorization** | Deciding what an authenticated user/device is allowed to do. |
| **Encryption** | Protecting data by making it unreadable without the proper key. |
| **Interoperability** | Different devices and systems working together. |
| **Scalability** | Ability to support growth in devices, users, or data. |
| **Edge computing** | Processing data near the device/source instead of sending everything to a remote cloud first. |
| **Edge analytics** | Analysing data locally near its source; useful for fast responses and reduced bandwidth. |

---

# Lab 05 — IoT Monitoring with Raspberry Pi and Ubidots Cloud

## 1. Thirty-second overview

A **DHT22 temperature/humidity sensor** is connected to a **Raspberry Pi**. A Python program reads the sensor values and sends them over the internet to **Ubidots**, using an API/device token. Ubidots stores the incoming variable data and shows it on a dashboard as a gauge, thermometer, chart, or table. Alerts can be configured for threshold conditions.

**Flow:** `DHT22 → Raspberry Pi → Python program → Internet/API → Ubidots device/variables → Dashboard/alerts`

## 2. Important components and keywords

| Keyword | Short meaning / role |
|---|---|
| **Raspberry Pi** | Linux-based single-board computer; runs Python and connects the sensor to the cloud. |
| **DHT22 / AM2302** | Digital sensor that measures both temperature and relative humidity. |
| **Python** | Programming language used here to read sensor values and send HTTP requests. |
| **Ubidots** | IoT cloud platform for collecting, visualising, monitoring, and acting on device data. |
| **Device** | A named/registered object in the Ubidots platform representing the physical system. |
| **Variable** | A measured or reported value belonging to a device, e.g., `temperature` or `humidity`. |
| **Device label** | Identifier used by the program/API to address a cloud device. |
| **API token** | Credential used to authenticate the program when it sends data to Ubidots. Keep it private. |
| **Payload** | The data body sent in a request; commonly contains variable names and values. |
| **HTTP POST** | HTTP request method commonly used to submit data to a server/API. |
| **JSON** | Text-based data format commonly used to represent key/value data in API requests. |
| **Dashboard/widget** | Visual display such as a gauge, thermometer, chart, or table. |
| **Threshold alert** | Notification/action triggered when a value crosses a configured limit. |
| **Retry** | Attempting a request again if a network/API request fails. |

## 3. Likely viva questions

**Q1. What is the aim of this experiment?**  
To read temperature/humidity using a DHT22 sensor connected to Raspberry Pi, upload the readings to Ubidots, and visualise/monitor them on a cloud dashboard.

**Q2. What does DHT22 measure?**  
Temperature and relative humidity. It provides a digital output and is also known as AM2302.

**Q3. Why use Raspberry Pi?**  
It can interface with sensors, run Python/Linux programs, and use Wi-Fi/Ethernet to send data to a cloud service.

**Q4. What is Ubidots?**  
An IoT cloud platform that receives device data, stores variables, displays dashboards, and can trigger events or notifications.

**Q5. How does data reach Ubidots?**  
The Python program reads the sensor, creates a payload, authenticates with an API token, and sends an HTTP request over the internet to the Ubidots API.

**Q6. Why is an API token needed?**  
It authenticates the device/program and controls access to the cloud account or device. It should not be shared publicly.

**Q7. What is the role of a dashboard?**  
It converts raw values into easy-to-read charts, gauges, thermometers, and tables for monitoring trends and current readings.

**Q8. Can Ubidots send alerts?**  
Yes. Events can be configured to notify users, for example when temperature moves outside a chosen range.

**Q9. What happens if the internet connection fails?**  
The upload may fail. The program should handle errors/retry; readings cannot reach the cloud until connectivity returns unless local buffering is implemented.

**Q10. What is the difference between a device and a variable in Ubidots?**  
A device represents the physical IoT system; a variable represents one data value measured or reported by it.

**Q11. Why use HTTP POST and JSON?**  
POST submits data to an API; JSON provides a structured, lightweight format for sending variable values.

**Q12. What can you troubleshoot if no values appear on the dashboard?**  
Check sensor wiring/pin selection, sensor library, internet connectivity, device/variable labels, API token, API response/status, and dashboard widget configuration.

## 4. Explain the setup in order

1. Connect the DHT22 to Raspberry Pi with the correct power, ground, and data wiring.
2. Install the required sensor library and Python dependencies.
3. Create an Ubidots account and a device.
4. Copy the device/API token into the local program securely.
5. Configure the device label and variable label(s), such as temperature.
6. Run the Python program: read sensor → build payload → send request.
7. Confirm incoming values in the Ubidots device page.
8. Add dashboard widgets and optional threshold alerts.

**One-line conclusion:** Sensor readings were acquired at the edge by Raspberry Pi and sent to Ubidots for cloud storage and visual monitoring.

---

# Lab 06 — IoT Cloud Application using ThingSpeak

## 1. Thirty-second overview

A sensor connected to a device such as Raspberry Pi, Arduino, ESP8266, or ESP32 generates data. The device sends readings to **ThingSpeak**, a cloud IoT analytics platform. A **channel** contains named fields; ThingSpeak graphs the values and can use MATLAB-based analysis and alerts.

**Flow:** `Sensor/device → HTTP or MQTT → ThingSpeak channel/fields → graphs/analysis/alerts`

## 2. Cloud computing: key terms

| Keyword | Short meaning |
|---|---|
| **Cloud computing** | On-demand computing, storage, and services delivered over a network. |
| **IoT cloud platform** | Cloud service designed to connect devices, collect data, manage devices, and provide analysis/visualisation. |
| **Scalability** | Adding resources as the number of devices/data grows. |
| **Elasticity** | Automatically adjusting resources to current demand. |
| **Pay-as-you-go** | Paying according to usage rather than buying all infrastructure upfront. |
| **Availability** | How often a service is accessible and working. |
| **Redundancy** | Duplicate components/data paths that reduce single points of failure. |
| **Disaster recovery** | Restoring service/data after a major failure. |
| **Data analytics** | Examining data to identify patterns, trends, or useful results. |
| **Predictive analytics** | Using past/current data and models to estimate future events or values. |
| **AI / ML** | Artificial intelligence / machine learning; techniques that infer patterns or make predictions from data. |
| **OTA update** | Over-the-air update: delivering firmware/software remotely through a network. |
| **Edge-cloud integration** | Processing some data locally and sending selected data to the cloud. |
| **SDK** | Software Development Kit: libraries/tools that help developers integrate a service. |
| **API key** | Credential used by an application to access a channel/API. |
| **Write API key** | Allows an application to write/update channel data. |
| **Read API key** | Allows authorised reading of private channel data. |
| **Channel** | ThingSpeak container for one IoT data stream/project. |
| **Field** | One data column/series in a channel, e.g., temperature or humidity. |
| **Channel ID** | Unique numeric identifier for a ThingSpeak channel. |
| **MATLAB Analysis** | ThingSpeak feature for processing/analyzing IoT data using MATLAB. |

## 3. Benefits of cloud for IoT

- **Scalability:** supports growth in devices and messages.
- **Cost efficiency:** reduces the need to own and maintain local servers.
- **Storage and processing:** stores large datasets and performs analytics.
- **Remote access:** users can view data from any internet-connected location.
- **Reliability:** backups and redundancy can improve availability.
- **Security:** supports authentication, encryption, and access control.
- **Integration:** connects to APIs, databases, AI/ML, and other applications.
- **Faster development:** ready-made services shorten setup and deployment time.

## 4. Cloud platform examples from the lab notes

| Platform | Short description |
|---|---|
| **AWS IoT Core** | Secure device communication and integration with AWS services; supports common IoT messaging protocols. |
| **Microsoft Azure IoT Hub** | Bi-directional device/cloud messaging, device provisioning, monitoring, and analytics integration. |
| **IBM Watson IoT Platform** | Device connectivity and analytics-oriented IoT services. |
| **Oracle IoT Cloud** | Enterprise/asset monitoring and predictive-maintenance use cases. |
| **ThingSpeak (MathWorks)** | IoT data collection, charts, and MATLAB-based analysis; useful for prototypes and learning. |
| **Particle Cloud** | Developer-oriented device connectivity and APIs. |
| **Siemens MindSphere / Industrial IoT offerings** | Industrial/manufacturing monitoring and analytics. |
| **GE Predix** | Industrial data analytics and predictive-maintenance focus. |
| **Google Cloud IoT Core** | **Historical note:** the service was retired in 2023; don’t describe it as a currently available managed service. |

## 5. Important cloud platform features

- Device connectivity and management.
- Data ingestion, storage, and stream processing.
- Real-time and historical analytics.
- Scaling and dynamic resource allocation.
- Authentication, encryption, privacy, and access control.
- Edge computing support.
- APIs and SDKs.
- Dashboards, reports, alerts, and notifications.
- Interoperability across different devices.
- Usage monitoring and billing.

## 6. ThingSpeak setup — memorise this sequence

1. **Create/sign in** to a ThingSpeak/MathWorks account.
2. Open **Channels → My Channels → New Channel**.
3. Enter the channel name and description.
4. Enable and name fields, e.g., Field 1 = Temperature, Field 2 = Humidity. The lab notes state that a channel can have up to **8 fields**.
5. **Save** the channel.
6. Open **API Keys** and note the **Channel ID**, **Write API Key**, and (if needed) **Read API Key**.
7. Connect the device/program and use HTTP or MQTT to upload readings.
8. View the auto-generated field charts; customise charts or use MATLAB Analysis if required.
9. Optionally configure alerts and choose whether the channel remains private or is shared publicly.

**Example HTTP update (illustrative):**
```text
https://api.thingspeak.com/update?api_key=YOUR_WRITE_API_KEY&field1=25.6&field2=70
```
This example submits 25.6 to Field 1 and 70 to Field 2. Use your own key; never publish it.

## 7. Likely viva questions

**Q1. What is ThingSpeak?**  
A cloud IoT platform used to collect, visualise, and analyse sensor data through channels and fields.

**Q2. What is a channel?**  
A container for a project's incoming data. Its fields represent separate measured values.

**Q3. What is the difference between Channel ID and API key?**  
The Channel ID identifies the channel; the API key authorises a particular action, such as writing data.

**Q4. Why do we need a Write API Key?**  
To authorise the device/program to upload readings to the channel.

**Q5. What is the purpose of a Read API Key?**  
To allow authorised access to read data from a private channel.

**Q6. How is data visualised in ThingSpeak?**  
Each enabled field can be displayed as a graph; MATLAB tools can provide further analysis.

**Q7. What is MQTT?**  
A lightweight publish/subscribe messaging protocol commonly used for IoT devices. A publisher sends messages to a topic through a broker; subscribers receive messages for topics they subscribe to.

**Q8. HTTP vs MQTT?**  
HTTP commonly uses request/response; MQTT uses lightweight publish/subscribe messaging and is useful for frequent IoT telemetry.

**Q9. What are the main advantages of cloud IoT?**  
Scalability, remote access, storage, analytics, integration, and reduced need to maintain local infrastructure.

**Q10. What is edge computing, and why is it useful with cloud?**  
Processing near the device reduces latency and bandwidth usage; the cloud can handle long-term storage and broader analysis.

**Q11. What is the difference between real-time and batch processing?**  
Real-time processing handles incoming data as it arrives; batch processing analyses a collected group of data later.

**Q12. Why keep a channel private?**  
To prevent unauthorised users from viewing data; access keys and permissions should be protected.

---

# Lab 07 — Raspberry Pi as a Web Server and Web Control of an Actuator

## 1. Thirty-second overview

The **Raspberry Pi** runs the **Apache web server** and hosts a web page. A user opens the Pi's IP address in a browser and presses a control such as ON or OFF. The web page sends a request to a server-side script (the lab uses Python) that controls an LED/bulb connected to the Pi.

**Flow:** `Browser/client → HTTP request over network → Apache on Raspberry Pi → Python/control logic → GPIO → LED/actuator`

This is web-based device control. It may work on a local network; access from outside the network requires suitable network configuration and security.

## 2. Key terms

| Keyword | Short meaning |
|---|---|
| **Web server** | Software that receives web requests and serves pages or responses. |
| **Apache HTTP Server** | Popular web-server software; can serve HTML pages and support dynamic behaviour through modules/scripts. |
| **Client** | The browser or application requesting a service. |
| **Server** | The system that receives requests and returns pages/data or performs a service. |
| **HTTP** | Hypertext Transfer Protocol; request/response protocol used by browsers and web servers. |
| **HTTPS** | HTTP protected using TLS encryption. |
| **URL** | Address identifying a web resource. |
| **IP address** | Network address used to identify/reach a device. |
| **Localhost / 127.0.0.1** | Refers to the current device itself. |
| **HTML** | Markup language that structures the content of a web page. |
| **CSS** | Styles the appearance/layout of a page. |
| **JavaScript** | Adds client-side interactivity and browser behaviour. |
| **Python** | Can run server-side logic and interact with Raspberry Pi GPIO. |
| **CGI (Common Gateway Interface)** | Mechanism for a web server to run a program/script to generate a response. |
| **GPIO** | General-Purpose Input/Output pins used to read signals or control components. |
| **Web GUI** | Graphical interface presented through a web browser. |
| **REST API** | Web interface that exposes resources/actions through standard HTTP methods and resource URLs. |
| **WebSocket** | Protocol that supports two-way communication over a persistent connection, useful for live updates. |
| **RPC** | Remote Procedure Call; requesting a function/action on another system. |
| **Telemetry** | Device measurements/status sent to a server or dashboard. |
| **Statelessness** | HTTP requests are generally independent; the server does not automatically remember earlier requests unless state/session mechanisms are added. |
| **Session** | Mechanism for maintaining user-specific state across requests. |
| **TLS / SSL** | Cryptographic protocols used to secure network communications; TLS is the modern successor to SSL. |

## 3. Why use web technology for IoT?

- **Interoperability:** standard protocols let different systems communicate.
- **Cross-platform access:** a browser can run on phones, tablets, and computers.
- **Convenience:** often no dedicated client application is needed.
- **Real-time communication:** WebSockets/server-sent events can provide low-latency updates.
- **Cloud integration:** APIs connect devices to storage, analytics, and dashboards.
- **Security options:** HTTPS/TLS and authentication can protect communication.
- **Scalability:** web services can be extended as more devices/users are added.

## 4. Choosing a web server — eight factors from the lab notes

1. **Size:** lightweight enough for the target hardware.
2. **Security:** TLS/HTTPS and authentication support.
3. **Stability and maturity:** reliable, maintained, and well tested.
4. **Platform agnostic:** works across the intended operating systems/devices.
5. **Simplicity:** straightforward integration and configuration.
6. **Clarity:** clear APIs and documentation; easy-to-understand integration.
7. **Licensing:** licence and cost suitable for the project.
8. **Support:** documentation, community, and vendor help where needed.

## 5. Apache commands to remember

```bash
sudo apt-get update
sudo apt-get install apache2 -y
sudo systemctl status apache2
sudo systemctl start apache2
sudo systemctl restart apache2
sudo systemctl stop apache2
hostname -I
cd /var/www/html
```

- The lab notes identify `/var/www/html/index.html` as the default page location.
- The default page can be tested on the Pi with `http://localhost/` or `http://127.0.0.1/`.
- From another device on the same network, use `http://<Pi-IP-address>/`.
- The lab places the web-control page in `/var/www/html/` and uses Python scripts for ON/OFF actions. Exact paths/permissions depend on how Apache and the script handler are configured.

## 6. Likely viva questions

**Q1. What is the aim of this experiment?**  
To configure Apache on Raspberry Pi and control an LED/bulb or other actuator using a browser-based web interface.

**Q2. What is Apache?**  
A web server that accepts HTTP requests and serves web pages or other responses.

**Q3. What is the role of Raspberry Pi?**  
It hosts the web server, runs control logic, and uses GPIO to operate the actuator.

**Q4. What happens when the user presses ON in the browser?**  
The browser sends a request to the Pi's web server; the server-side program processes it and changes the appropriate GPIO output to switch the actuator on.

**Q5. What is the difference between client and server?**  
The client initiates a request; the server receives it and returns a response or performs the requested operation.

**Q6. What is GPIO?**  
General-Purpose Input/Output pins on the Pi used to interface with external hardware.

**Q7. What is the purpose of HTML?**  
It defines the structure and elements of the web page, such as headings and ON/OFF controls.

**Q8. Why use Python?**  
It can implement server-side control logic and interact with the Raspberry Pi's GPIO.

**Q9. How do you find the Pi's IP address?**  
Run `hostname -I` in the terminal.

**Q10. What is the difference between HTTP and HTTPS?**  
HTTPS protects HTTP communication with TLS encryption and helps provide confidentiality and server authentication.

**Q11. What is a REST API?**  
A web interface that exposes resources or actions using URLs and HTTP methods such as GET, POST, PUT, and DELETE.

**Q12. What are WebSockets?**  
They provide persistent, two-way communication between client and server, useful when devices need to push live updates.

**Q13. Why is security important for a web-controlled actuator?**  
An unauthorised person could observe data or operate physical devices. Use authentication, HTTPS where applicable, least privilege, and restrict network access.

**Q14. What is the stateless nature of HTTP?**  
Each request is generally handled independently; if an application needs to remember a user or state across requests, it uses sessions, tokens, or other mechanisms.

**Q15. What should you check if the page opens but the LED does not switch?**  
Check the Pi IP/network, server and script logs, file paths/permissions, GPIO pin configuration, wiring, component power, and whether the request reaches the correct script.

## 7. Troubleshooting checklist

- Confirm Apache is running.
- Confirm the browser is using the correct Pi IP address.
- Confirm the HTML page is in the configured web directory.
- Confirm the request reaches the intended Python/control script.
- Confirm the script has the necessary permissions and GPIO access.
- Check GPIO number, wiring, ground, and actuator interface.
- Do not expose a control endpoint publicly without proper authentication and network security.

**One-line conclusion:** A browser sends a web request to Apache on Raspberry Pi, and server-side logic operates the connected actuator.

---

# Lab 09 — Arduino Bluetooth IoT Control using an Android App

## 1. Thirty-second overview

An Android phone runs an app made with **MIT App Inventor**. The phone pairs with the **HC-05 Bluetooth module**, which is connected to an **Arduino Uno** through serial TX/RX. When the user presses ON or OFF, the app sends a character/command over Bluetooth. Arduino reads it and changes an output pin to control an LED/bulb (using an appropriate driver/relay circuit for a real bulb).

**Flow:** `Android app → Bluetooth link → HC-05 → UART/serial → Arduino → output/driver → LED or bulb`

## 2. Key terms

| Keyword | Short meaning |
|---|---|
| **Arduino Uno** | Microcontroller development board used to read commands and control outputs. |
| **Bluetooth** | Short-range wireless communication technology often used for personal-area connections. |
| **Bluetooth PAN** | Personal Area Network formed by nearby Bluetooth devices. |
| **HC-05** | Classic Bluetooth serial module that can operate in master or slave role. |
| **Serial communication** | Data sent sequentially, bit by bit, over a communication link. |
| **UART / USART** | Hardware/interface for asynchronous (UART) or synchronous/asynchronous (USART) serial communication. |
| **TXD** | Transmit-data pin. |
| **RXD** | Receive-data pin. |
| **VCC** | Supply-voltage pin. |
| **GND** | Ground reference. |
| **EN / KEY** | HC-05 control pin used to enter AT command mode on supported boards. |
| **STATE** | Pin that can indicate connection status on the module/board. |
| **Baud rate** | Serial signalling speed, expressed in symbols per second; common configured serial rates include 9600 baud. |
| **Pairing** | Establishing a trusted relationship between Bluetooth devices. |
| **Data mode** | HC-05 mode for exchanging normal data. |
| **AT command mode** | Configuration mode for changing module settings using AT commands. |
| **MIT App Inventor (AI2)** | Visual, block-based environment for building mobile applications. |
| **GUI** | Graphical User Interface: buttons, labels, lists, and other visible controls. |
| **Blocks** | Drag-and-drop logic components in App Inventor instead of writing all code textually. |
| **MIT AI2 Companion** | Phone app used to test an App Inventor project live during development. |
| **APK** | Android Package Kit; installable package for an Android application. |
| **BluetoothClient** | App Inventor component used by an app to connect to and exchange data with Bluetooth devices. |
| **ListPicker** | App Inventor component often used to list paired Bluetooth devices and select one. |
| **Edge computing** | Local processing at the Arduino/near-device level, rather than requiring a cloud round trip for every command. |
| **Edge analytics** | Analysing data locally near its source. For this experiment, the main local action is command handling/control; advanced analytics are not required. |

## 3. HC-05 pins and modes

| Pin | Role |
|---|---|
| **VCC** | Module supply. Check the breakout-board specifications; the onboard regulator does not necessarily make every signal pin 5 V tolerant. |
| **GND** | Common ground. |
| **TXD** | Serial data transmitted from HC-05 to Arduino's receive pin. |
| **RXD** | Serial data received by HC-05 from Arduino's transmit pin. |
| **EN/KEY** | Used to enter AT command mode on supported HC-05 boards. |
| **STATE** | May indicate whether a Bluetooth connection is active. |

**Cross-connect serial pins:** HC-05 TXD → Arduino RX; Arduino TX → HC-05 RX.  
**Voltage note:** HC-05 UART logic is typically 3.3 V. Use suitable level shifting/division on the Arduino TX → HC-05 RX path when required by the particular module board. Confirm the board's supply and logic-level specifications before wiring.

**Two modes:**
- **Data mode:** normal data exchange between devices.
- **Command mode:** AT commands configure settings. The lab notes list 38400 baud as the common command-mode rate and 9600 baud as the common data-mode default; module variants/configuration may differ.

**Connection indicator:** The lab notes describe a red LED blinking rapidly while unconnected and blinking more slowly after a connection is made.

## 4. MIT App Inventor — what to say

MIT App Inventor is a visual, block-based development environment maintained by MIT. Users drag interface components into a Designer view and connect logic blocks in a Blocks view. The app can be tested with MIT AI2 Companion and built as an Android APK. The lab example uses a device picker plus ON/OFF buttons and a BluetoothClient component.

**Typical app logic:**
1. List available paired Bluetooth devices.
2. User selects the HC-05 device.
3. App connects using the selected device address.
4. ON button sends an ON command (for example, `"1"`).
5. OFF button sends an OFF command (for example, `"0"`).
6. Arduino receives the command over serial and changes its output.

## 5. Experiment steps — memorise this order

1. Wire the HC-05 to Arduino (power, ground, TX, RX) and connect the output/LED circuit.
2. Upload Arduino code that reads serial commands and controls the output.
3. Create the Android interface in MIT App Inventor.
4. Add a ListPicker, BluetoothClient, and ON/OFF controls; create the block logic.
5. Test live using MIT AI2 Companion, or build an APK for installation.
6. Pair the phone with HC-05 in the phone's Bluetooth settings.
7. Connect from the app, then test ON/OFF commands.
8. Confirm the LED/output follows the commands.

## 6. Likely viva questions

**Q1. What is the aim of the experiment?**  
To control an Arduino-connected LED/bulb wirelessly from an Android phone using Bluetooth and an app built with MIT App Inventor.

**Q2. What is HC-05?**  
A Bluetooth serial module that lets a microcontroller exchange serial data wirelessly with another Bluetooth device.

**Q3. Why is Bluetooth used here?**  
It provides a short-range wireless link without requiring an internet connection or cloud service.

**Q4. What is the role of Arduino?**  
It receives the command from HC-05 over serial and controls the output pin according to the command.

**Q5. What is the role of MIT App Inventor?**  
It provides a visual way to design the phone interface and program its behaviour using blocks.

**Q6. What is the difference between data mode and AT command mode?**  
Data mode transfers application data; AT command mode is used to configure the HC-05 module.

**Q7. What is pairing?**  
The process of establishing a trusted Bluetooth relationship before connecting/exchanging data.

**Q8. What do TX and RX mean?**  
TX transmits serial data; RX receives serial data. They are normally cross-connected between the two devices.

**Q9. What is baud rate?**  
The rate of serial signalling. The sender and receiver must use compatible serial settings.

**Q10. What is an APK?**  
The installable package format for Android apps.

**Q11. What is MIT AI2 Companion?**  
A phone app used to test an App Inventor project without first packaging it as a standalone APK.

**Q12. Does this system need the internet?**  
No. The phone and HC-05 communicate locally over Bluetooth. Internet is not needed for the basic ON/OFF control.

**Q13. What is edge computing in this experiment?**  
The Arduino handles the command and controls the output locally, avoiding the delay and dependency of a cloud round trip.

**Q14. What is edge analytics?**  
Analysing data near where it is produced. This lab primarily demonstrates local control; it does not require complex analytics.

**Q15. Why should a real bulb not always be connected directly to an Arduino pin?**  
A microcontroller pin cannot safely supply the voltage/current required by many bulbs. Use a correctly rated driver/relay interface and proper electrical isolation/safety measures.

**Q16. What should you check if the app cannot connect?**  
Confirm Bluetooth is enabled, HC-05 is powered and paired, the correct device is selected, wiring is correct, serial baud rate matches, and the module is not already connected elsewhere.

**Q17. What should you check if the app connects but the output does not change?**  
Check what text/byte the app sends, what command Arduino expects, TX/RX wiring, common ground, serial configuration, code logic, output pin, and circuit wiring.

**Q18. What is the difference between Bluetooth control and cloud control?**  
Bluetooth control is usually short-range and local; cloud control sends data/commands through an internet-connected cloud service and can enable remote access from farther away.

---

# High-value comparison questions

## 1. Ubidots vs ThingSpeak

| Point | Ubidots | ThingSpeak |
|---|---|---|
| Main role in these labs | Device data monitoring and dashboard creation | Channel-based data collection, graphing, and analysis |
| Data organisation | Devices and variables | Channels and fields |
| Authentication used in the lab | Device/API token | Channel ID plus API keys |
| Visualisation | Gauges, thermometers, charts, tables, dashboards | Field charts and dashboards/analysis tools |
| Example | Raspberry Pi + DHT22 sends temperature | A device sends temperature/humidity into channel fields |

## 2. Raspberry Pi vs Arduino Uno

| Point | Raspberry Pi | Arduino Uno |
|---|---|---|
| Type | Single-board computer | Microcontroller board |
| Typical software | Linux, Python and other applications | Firmware/sketch, commonly written in Arduino C/C++ style |
| Best suited for these labs | Sensor-to-cloud Python client; hosting Apache/web logic | Reading Bluetooth commands and controlling outputs |
| Networking | Can use Wi-Fi/Ethernet via its setup/peripherals | Usually needs a communication module/shield for networking |
| System role | Can be a local server/gateway/edge computer | Local embedded controller |

## 3. Bluetooth vs Wi-Fi vs Cloud

- **Bluetooth:** short-range device-to-device communication; works locally without internet.
- **Wi-Fi:** connects devices to a local wireless network and often provides internet access through a router.
- **Cloud:** remote infrastructure for storing, analysing, visualising, or routing data; usually accessed through the internet.
- **Important distinction:** Bluetooth/Wi-Fi are communication technologies; a cloud platform is a remote service environment.

## 4. HTTP vs MQTT vs Bluetooth serial

- **HTTP:** web request/response; common for REST APIs and uploading sensor data.
- **MQTT:** lightweight publish/subscribe protocol; good for telemetry and many-to-many messaging.
- **Bluetooth serial:** short-range wireless link that presents a serial-data interface between paired devices.

## 5. Sensor vs actuator

- **Sensor:** input — measures the environment, e.g., DHT22 temperature/humidity.
- **Actuator:** output — changes something, e.g., a lamp, motor, or relay.
- A single IoT system can contain both: sense data, process it, then control an actuator.

---

# Diagram practice (draw these from memory)

## A. Ubidots monitoring
```text
[DHT22 sensor]
      │ temperature / humidity
      ▼
[Raspberry Pi + Python]
      │ HTTP request + API token
      ▼
[Internet / Ubidots cloud]
      │ store variables
      ▼
[Dashboard: gauge / chart / table / alerts]
```

## B. ThingSpeak cloud application
```text
[Sensor] → [Arduino / ESP / Raspberry Pi]
                     │ HTTP or MQTT + API credentials
                     ▼
             [ThingSpeak channel]
              ├─ Field 1: Temperature
              └─ Field 2: Humidity
                     ▼
             [Charts / MATLAB analysis]
```

## C. Raspberry Pi web server
```text
[Phone / PC browser]
         │ HTTP request (ON/OFF)
         ▼
[Apache web server on Raspberry Pi]
         │
         ▼
[Python/control script]
         │ GPIO output
         ▼
[Driver/relay as needed] → [LED / actuator]
```

## D. Arduino Bluetooth control
```text
[Android app: ON / OFF]
          │ Bluetooth
          ▼
      [HC-05 module]
          │ UART serial TX/RX
          ▼
      [Arduino Uno]
          │ output pin
          ▼
 [LED / suitable driver / bulb]
```

---

# Rapid-fire revision: answer in one or two sentences

1. **What is an IoT dashboard?** A visual interface for device values, charts, status, and alerts.
2. **Why is a token/API key important?** It authenticates a client and authorises access; it must remain secret.
3. **What is a payload?** The data carried in a request/message.
4. **What is JSON?** A lightweight text format for structured key/value data.
5. **What is an API?** A defined way for software components to communicate.
6. **What is a web server?** Software that accepts web requests and returns pages/data or runs server-side logic.
7. **What is Apache used for in this lab?** Serving the control webpage from Raspberry Pi.
8. **What is GPIO used for?** Reading input signals and controlling external components.
9. **What is a serial port?** An interface for sequential data communication.
10. **What does HC-05 do?** Provides a Bluetooth wireless serial link.
11. **What does a ListPicker do in the app?** Lets the user select a Bluetooth device from a list.
12. **What is a cloud variable?** A named value associated with a device, such as temperature.
13. **What is a cloud channel field?** One data series within a ThingSpeak channel.
14. **Why are charts useful?** They reveal trends and changes more clearly than isolated values.
15. **What is a threshold?** A configured limit used to trigger a warning/action.
16. **What is latency?** Delay between sending data/command and its arrival or effect.
17. **What is authentication vs authorisation?** Authentication verifies identity; authorisation grants permissions.
18. **What is scalability?** Ability to grow to handle more devices/data.
19. **What is interoperability?** Different devices/platforms working together.
20. **What is a relay?** An electrically controlled switch, often used to control a higher-power load through a suitable interface.
21. **Why is a common ground often needed?** It provides a shared voltage reference for connected low-voltage circuits.
22. **What does “real-time” mean here?** Data/control is updated with sufficiently low delay for the application's needs; it does not necessarily mean zero delay.
23. **What is local control?** The device performs the action nearby without needing a cloud round trip.
24. **What is remote monitoring?** Viewing device data from another location through a network/cloud.
25. **What is the key security concern across these labs?** Protect credentials and restrict who can view data or control physical devices.

---

# Last-minute viva strategy

- Start each answer with the **purpose**, then name the **main components**, then explain the **data/command flow**.
- If asked “why this component?”, answer with its role: DHT22 measures; Raspberry Pi runs Python; Ubidots/ThingSpeak stores and visualises; Apache serves pages; HC-05 carries Bluetooth serial data; Arduino controls the output.
- If asked to troubleshoot, trace the path one step at a time: **wiring → program → communication → authentication/network → cloud/server → dashboard/output**.
- Be clear about **monitoring vs control**: monitoring reads/displays values; control sends a command that changes an actuator.
- For real electrical loads, mention the correct driver/relay and safe isolation rather than implying a mains bulb should connect directly to a GPIO pin.
