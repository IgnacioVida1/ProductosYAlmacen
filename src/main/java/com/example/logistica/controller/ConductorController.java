package com.example.logistica.controller;

import com.example.logistica.entity.Conductor;
import com.example.logistica.service.ConductorService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/conductores")
public class ConductorController {

    private final ConductorService conductorService;

    public ConductorController(ConductorService conductorService) {
        this.conductorService = conductorService;
    }

    @PostMapping("/conductores")
    public ResponseEntity<Conductor> registrarConductor(@RequestBody Conductor c){
        return ResponseEntity.ok(conductorService.registrarConductor(c));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Conductor> consultarConductor(@PathVariable Long id){
        return ResponseEntity.ok(conductorService.consultarConductor(id));
    }

    @GetMapping("/disponibles")
    public ResponseEntity<List<Conductor>> conductoresDisponibles(){
        return ResponseEntity.ok(conductorService.consultarDisponibilidadConductores());
    }

}
