import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Home from './home'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      
        
          <Route exact path = "/">
            <Home/>
          </Route>

          <Route exact path = "/app">
            <App/>
          </Route>

    </Router>

  </React.StrictMode>,
)
