 $(document).ready(function() {
      $('.select2').select2({
        theme: 'default',
        width: '100%',
        placeholder: function() {
          return $(this).data('placeholder') || 'Choose options...';
        },
        allowClear: false,
        closeOnSelect: false
      });
    });