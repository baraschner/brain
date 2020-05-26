import React from 'react';
import './App.css';
import AllUsers from './AllUsers.js'
import logo from './brain.png';
import AppBar from '@material-ui/core/AppBar';
import ToolBar from '@material-ui/core/Toolbar';
import BottomNavigation from '@material-ui/core/BottomNavigation';


class App extends React.Component {

    render() {

        return (
            <React.Fragment>
                <AppBar position="static">
                    <ToolBar>
                        <img alt="" src={logo} width='45' height='45'/>
                        brain
                    </ToolBar>
                </AppBar>
                <AllUsers/>
                <BottomNavigation>
                    <p>Icons by <a href="https://icons8.com/">Icons8</a></p>
                </BottomNavigation>
            </React.Fragment>
        );
    }

}


export default App;
