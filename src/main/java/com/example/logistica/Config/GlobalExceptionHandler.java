package com.example.logistica.Config;

import com.example.logistica.exception.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BadRequestException.class)
    public ResponseEntity<String> handleResourceNotFound(BadRequestException ex) {
        return new ResponseEntity<>( "Request mal hecho o en conflicto: " + ex.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<String> handleResourceConflictException(NotFoundException ex) {
        return ResponseEntity.status(HttpStatus.CONFLICT).body("Recurso no encontrado: " + ex.getMessage());
    }
}
