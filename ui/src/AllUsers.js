import React from 'react';
import './App.css';
import User from './components/user/user'
import Snapshot from "./components/snapshot/snapshot";


class AllUsers extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            users: null,
            displaySnapshot: false,
            displayUserId: null
        };
        this.closeSnapshots = this.closeSnapshots.bind(this)
        this.displaySnapshots= this.displaySnapshots.bind(this)

    };


    displaySnapshots(user_id) {
        this.setState({displaySnapshot: true, displayUserId: user_id})
    }

    closeSnapshots() {
        this.setState({displaySnapshot: false});
    }

    render() {

        if (this.state.users == null) {
            return 'loading ...';
        }
        let snapshot = null
        if (this.state.displaySnapshot) {
            snapshot = <Snapshot userId={this.state.displayUserId} close={this.closeSnapshots}/>

        }
        return (
            <React.Fragment>
                {this.state.users.map((user) =>
                    <User key={user.userId} userId={user.userId}
                          onClick={this.displaySnapshots.bind(this, user.userId)}/>)
                }
                {snapshot}
            </React.Fragment>
        );
    }


    componentDidMount() {
        fetch(`${window.apisrv}/users`)
            .then(response => response.json())
            .then(data => this.setState({users: data}));
    }
}

export default AllUsers;
