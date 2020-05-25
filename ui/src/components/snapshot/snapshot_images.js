import React from 'react';


class SnapshotImages extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pose: null,
        };
    }

    componentDidMount() {
        if (this.props.snapshotId) {

            fetch(`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/colorImage/data`)
                .then(data => this.setState({feelings: data}));
        }
    };

    render() {
        if (this.props.snapshotId === null) {
            return 'loading...'
        }

        return (
            <div>

                <img width={300} height={300} alt="Color Image"
                     src={`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/colorImage/data`}/>


                <img width={300} height={300} alt="Depth Image"
                     src={`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/depthImage/data`}/>

            </div>
        );

    }

}

export default SnapshotImages;
