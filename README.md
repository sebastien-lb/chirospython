# Chirospython

### How to use

```python

import chirospython as chp 


@chp.app.route('/off')
def off():
    chp.save_local_state(0, "state")
    led.off()
    chp.send_status(0, "state")

    return chp.Response(
        status=200
    )


@chp.app.route('/switch', methods=['POST'])
def switch():
    state = 1 - chp.get_saved_state("state")
    if state:
        led.on()
    else:
        led.off()

    chp.save_local_state(state, "state")

    chp.send_status(state, "state")
    return chp.Response(
        "status: {}".format(data['value']),
        status=200
    )


chp.launch_app(5006)
```