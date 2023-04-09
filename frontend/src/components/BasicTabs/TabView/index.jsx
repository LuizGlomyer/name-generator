import React from "react";

import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import Switch from '@mui/material/Switch';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';
import ReplayIcon from '@mui/icons-material/Replay';



import '../tabs.scss';
import { useState } from "react";
import Api from "../../../api";

function EnglishNameTab(props) {
  const [error, setError] = useState(false);
  const [errorMessage, setErrorMessage] = useState(null);
  const { state, dispatch } = props.reducer;
  const tabName = props.tabName;
  const min = 1;
  const max = 100;

  function handleInput(event) {
    setError(false);
    setErrorMessage(null);
    const value = event.target.value;
    const parsedValue = parseInt(value);

    if (parsedValue) {
      if (parsedValue > max)
        dispatch({ type: "updateQuantity", value: max });
      else if (parsedValue < min) {
        setError(true);
        setErrorMessage("Only positive numbers");
        dispatch({ type: "updateQuantity", value: parsedValue });
      }
      else
        dispatch({ type: "updateQuantity", value: parsedValue });
    }
    else {
      dispatch({ type: "updateQuantity", value: value });
      if (value !== '') {
        setError(true);
        setErrorMessage("Only numbers");
      }
    }
  }

  function handleRadioSelection(event) {
    dispatch({ type: "setRadioSelection", tab: tabName, value: event.target.value });
  }

  async function handleGenerate() {
    dispatch({ type: "loadingTrue" });
    await new Promise(r => setTimeout(r, 2000));
    let route = state.radioSelection[tabName];

    if (tabName === "brazillianName")
      route = "br-" + route;
    else if (tabName === "englishName")
      route = "en-" + route;
    const response = await Api.get(route, state.quantity);
    dispatch({ type: "setItems", tab: tabName, value: response });
    dispatch({ type: "loadingFalse" });
    console.log(response)
    console.log(state)
  }

  return (
    <div className="flex">
      {
        (props.brazillian || props.english) &&
        <FormControl>
          <FormLabel id="demo-radio-buttons-group-label">Type</FormLabel>
          <RadioGroup
            aria-labelledby="demo-radio-buttons-group-label"
            defaultValue="female"
            name="radio-buttons-group"
            value={state.radioSelection[tabName]}
            onChange={handleRadioSelection}
          >
            <FormControlLabel value="male" control={<Radio />} label="Male" />
            <FormControlLabel value="male-complete" control={<Radio />} label="Male Complete" />
            <FormControlLabel value="female" control={<Radio />} label="Female" />
            <FormControlLabel value="female-complete" control={<Radio />} label="Female Complete" />
            {
              props.brazillian &&
              <FormControlLabel value="surname" control={<Radio />} label="Surname" />
            }
          </RadioGroup>
        </FormControl>
      }

      <div className="flex-column parameters">
        <TextField
          id="number-quantity"
          value={state.quantity}
          onChange={handleInput}
          type="number"
          label="Quantity"
          variant="outlined"
          helperText={errorMessage}
          error={error}

        />
        <Button variant="contained" onClick={handleGenerate}>Generate</Button>
      </div>

      <div className="flex-column parameters">
        {
          props.fantasy &&
          <>
            <FormGroup>
              <FormControlLabel control={<Switch defaultChecked />} label="uncommon letters" />
            </FormGroup>
            <TextField

              value={state.quantity}
              onChange={handleInput}

              label="Letters"
              variant="outlined"
              helperText={errorMessage}
              error={error}

            />
            <Tooltip title="Reset to defaults">
              <IconButton>
                <ReplayIcon />
              </IconButton>
            </Tooltip>
          </>
        }
      </div>

      <Divider className="vertical-divider" orientation="vertical" />
      <div className="description">
        {

         // <p>Description here Praesent dui lorem, venenatis sed tempus a, suscipit a enim. Donec sed finibus risus, at ullamcorper sem. Praesent auctor odio at interdum sodales. Sed bibendum ullamcorper finibus. Fusce malesuada lorem in elit volutpat, sit amet aliquet nunc posuere. Ut iaculis tempus arcu vitae lobortis. Fusce eget ullamcorper mauris.</p>
        }
      </div>
    </div>
  );
}

export default EnglishNameTab;