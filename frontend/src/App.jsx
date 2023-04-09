import { useEffect, useState } from 'react'
import './App.scss'

import FormControlLabel from '@mui/material/FormControlLabel';
import FormGroup from '@mui/material/FormGroup';

import Switch from '@mui/material/Switch';

import Avatar from '@mui/material/Avatar';
import Divider from '@mui/material/Divider';

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';

import ContentCopyIcon from '@mui/icons-material/ContentCopy';

import Paper from '@mui/material/Paper';



import CircularProgress from '@mui/material/CircularProgress';
import SimpleSnackbar from './components/SimpleSnackbar';
import BasicTabs from './components/BasicTabs';


import Api from './api';
import { getReducer } from './reducer';




function App() {
  const [state, dispatch] = getReducer();
  const [items, setItems] = useState({});
  const [quantity, setQuantity] = useState(1);
  const [generatedQuantity, setGeneratedQuantity] = useState(50);

  const teste = { 1: 'Adalberto', 2: 'Ibérico' }

  

  function handleItemClick(item) {
    navigator.clipboard.writeText(item.target.innerText)
    dispatch({ type: "snackbarOpen" });
  }


  return (
    <div className="App">
      <div className='title'>
        <span className='title-word-1'>Random</span>
        <span className='title-word-2'>name</span>
        <span className='title-word-3'>generator</span>
      </div>

      <Paper id='paper' elevation={3}>
        <BasicTabs quantity={quantity} setQuantity={setQuantity} reducer={{ state, dispatch }} />

        {
          state.loading
            ? <div className='loading-circle'><CircularProgress /></div>
            :
            <List>
              {
                Object.keys(state.items[state.activeTab]).map((index) => {
                  const key = state.items[state.activeTab][index];
                  return (
                    <>
                      <ListItemButton key={`ItemButton-${index}-${key}`} onClick={handleItemClick}>
                        <ListItemIcon key={`ItemIcon-${index}-${key}`}>
                          <ContentCopyIcon key={`Icon-${index}-${key}`} />
                        </ListItemIcon >
                        <ListItemText key={`ItemText-${index}-${key}`} primary={state.items[state.activeTab][index]} />
                        {
                          //<Avatar alt="Cindy Baker" src="https://picsum.photos/200" />
                        }
                      </ListItemButton>

                    </>
                  );
                }
                )
              }
            </List>
        }

        <SimpleSnackbar reducer={{ state, dispatch }} />
      </Paper>
    </div>
  );
}

export default App
