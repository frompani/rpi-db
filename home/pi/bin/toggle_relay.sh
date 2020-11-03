#!/bin/bash

# Common path for all GPIO access
BASE_GPIO_PATH=/sys/class/gpio

case "$1" in 
	r1)
	  pin=14
	  ;;
	r2)
          pin=15
          ;;
	r3)
          pin=17
          ;;
	r4)
          pin=18
          ;;

       *)
            echo $"Usage: $0 {specificare il  relay: r1,r2,r3,r4}"
            exit 1
 
esac


# Assign names to states
ON="0"
OFF="1"

# Utility function to export a pin if not already exported
exportPin()
{
  if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
    echo "$1" > $BASE_GPIO_PATH/export
  fi
}

# Utility function to set a pin as an output
setOutput()
{
  echo "out" > $BASE_GPIO_PATH/gpio$1/direction
  echo "1" > $BASE_GPIO_PATH/gpio$1/value

}

# Utility function to change state of a light
setLightState()
{
  echo $2 > $BASE_GPIO_PATH/gpio$1/value
}

# Ctrl-C handler for clean shutdown
shutdown()
{
  exit 0
}

#trap shutdown SIGINT

# Export pins so that we can use them
exportPin $pin

# Set pins as outputs
setOutput $pin


setLightState $pin $ON
sleep 0.5
setLightState $pin $OFF

