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
        this.close_snapshot = this.close_snapshot.bind(this)

    };


    display_snapshots(user_id) {
        this.setState({displaySnapshot: true, displayUserId: user_id})
    }

    close_snapshot() {
        this.setState({displaySnapshot: false});
    }

    render() {

        if (this.state.users == null) {
            return 'loading ...';
        }
        let snapshot = null
        if (this.state.displaySnapshot) {
            snapshot = <Snapshot userId={this.state.displayUserId} close={this.close_snapshot}/>

        }
        return (
            <React.Fragment>
                {this.state.users.map((user) =>
                    <User key={user.userId} userId={user.userId}
                          onClick={this.display_snapshots.bind(this, user.userId)}/>)
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
