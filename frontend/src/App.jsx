import { useState } from 'react'
import './App.scss'
import Button from '@mui/material/Button';


import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import FormGroup from '@mui/material/FormGroup';

import Switch from '@mui/material/Switch';
import ReplayIcon from '@mui/icons-material/Replay';
import TextField from '@mui/material/TextField';
import Avatar from '@mui/material/Avatar';
import Divider from '@mui/material/Divider';

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';

import Paper from '@mui/material/Paper';

import DeleteIcon from '@mui/icons-material/Delete';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';

import CircularProgress from '@mui/material/CircularProgress';
import SimpleSnackbar from './components/SimpleSnackbar';
import BasicTabs from './components/BasicTabs';




function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <div className='title'>
        <span className='title-word-1'>Random</span>
        <span className='title-word-2'>name</span>
        <span className='title-word-3'>generator</span>
      </div>

      <Paper elevation={3} >
      <BasicTabs/>
        <Button variant="contained" onClick={() => alert("click")}>Hello World</Button>
        <FormControl>
          <FormLabel id="demo-radio-buttons-group-label">Gender</FormLabel>
          <RadioGroup
            aria-labelledby="demo-radio-buttons-group-label"
            defaultValue="female"
            name="radio-buttons-group"
          >
            <FormControlLabel value="female" control={<Radio />} label="Female" />
            <FormControlLabel value="male" control={<Radio />} label="Male" />
            <FormControlLabel value="other" control={<Radio />} label="Other" />
          </RadioGroup>
        </FormControl>

        <FormGroup>
          <FormControlLabel control={<Switch defaultChecked />} label="Label" />
          <FormControlLabel disabled control={<Switch />} label="Disabled" />
        </FormGroup>


        <TextField id="outlined-basic" label="Outlined" variant="outlined" />
        <Avatar alt="Cindy Baker" src="/static/images/avatar/3.jpg" />


        <List>
          <ListItem disablePadding>
            <ListItemButton>
              <ListItemText primary="Trash" />
            </ListItemButton>
          </ListItem>
          <Divider variant="middle" />
          <ListItem disablePadding>
            <ListItemButton component="a" href="#simple-list">
              <ListItemText primary="Spam" />
            </ListItemButton>
          </ListItem>
        </List>
        <Tooltip title="Reset to defaults">
          <IconButton>
            <ReplayIcon />
          </IconButton>
        </Tooltip>
        <CircularProgress />

        <SimpleSnackbar/>
        



      </Paper>


    </div>
  );
}

export default App
