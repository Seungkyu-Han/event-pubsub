# Event Pub/Sub Library

A simple and flexible asynchronous Event Pub/Sub library for Python.

---

## 🚀 Installation

Install via pip:

```bash
pip install event-pubsub
```

Or install locally for development:

```bash
pip install -e .
```

---

## 📦 Usage


### 1. Subscribe to an event

```python
from event_pubsub import subscriber

@subscriber.subscribe(event_type="hello")
def event_handler(name: str):
    print(f'hello {name} from sync')
```

---

### 2. publish an event

```python
from event_pubsub import publisher

async def say_hello(name: str):
    await publisher.publish('hello', name)
    return {"message": "success"}
```

---

### 3. Passing multiple arguments

```python
from event_pubsub import subscriber

@subscriber.subscribe(event_type="hello")
async def handle_message(user_id: int, message: str):
    print(user_id, message)

```

---

### 4. Multiple handlers

```python
from event_pubsub import subscriber

@subscriber.subscribe("event")
async def handler1(data):
    print("handler1", data)

@subscriber.subscribe("event")
async def handler2(data):
    print("handler2", data)
```

---

## ⚙️ Configuration

### Event Types

Events are identified by string keys:

```python
"user_created"
"order_completed"
"message_received"
```

---

### Argument Passing

The `emit` method supports flexible arguments:

```python
from event_pubsub import publisher

await publisher.publish("event", 1, 2, 3)
```


---

## 📄 License

MIT License
