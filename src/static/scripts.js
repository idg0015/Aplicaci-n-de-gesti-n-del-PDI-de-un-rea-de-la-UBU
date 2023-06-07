const center = (data, row, col) => {
    if (row) {
        return {class: 'gridjs-td text-center'};
    } else {
        return {};
    }
};